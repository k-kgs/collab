import os
from django.shortcuts import render

from .models import Project, ProjectUserMapping
from ..user.models import User
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class HealthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            return Response(
                {
                    "is_success": True,
                    "message": "Project Health is UP",
                    "data": None
                },
                status = status.HTTP_200_OK
            )
        except Exception as ex:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Checking Project Health",
                    "data": None
                },
                status = status.HTTP_200_OK
            )
        
class ProjectListView(APIView):
    def get(self, request, format=None):
        try:
            if not request.user.is_authenticated:
                return Response(
                    {
                        "is_success": False,
                        "message": "user must login to access",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            project_list = list()
            user_projects = ProjectUserMapping.objects.filter(
                user_id = request.user.id, #can change to user = request.user
                is_active = True,
                is_owner = True
            )
            for item in user_projects:
                project = item.project
                project_list.append(
                    {
                        "id": project.id,
                        "name": project.name,
                        "description": project.description,
                        "start_date": project.start_date,
                        "estimated_delivery_date": project.estimated_delivery_date
                    }
                )
            return Response(
                        {
                            "is_success": True,
                            "message": "Project list for " + request.user.email,
                            "data": {
                                "my_project": project_list,
                                "shared_project": [
                                    {
                                        "name": "SharedProject1",
                                        "description": "Description for SharedProject1",
                                        "start_date": "2024-05-23",
                                        "estimated_delivery_date": "2024-05-28"
                                    },
                                    {
                                        "name": "SharedProject2",
                                        "description": "Description for SharedProject2",
                                        "start_date": "2024-05-23",
                                        "estimated_delivery_date": "2024-05-28"
                                    }
                                ]
                            }
                        },
                        status=status.HTTP_200_OK
                    )
        except Exception as Exc:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While fetching Project List",
                    "data": Exc.__str__()
                },
                status = status.HTTP_200_OK
            )

class ProjectView(APIView):
    def get(self, request, format=None):
        try:
            print("request.user",request.user)
            if not request.user.is_authenticated:
                return Response(
                    {
                        "is_success": False,
                        "message": "user must login to access",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            project_id =  request.query_params.get('project', None)
            print("project_id",project_id)
            if project_id is None:
                return Response(
                    {
                        "is_success": False,
                        "message": "Invalid Project Id",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            project = Project.objects.filter(id=project_id).first()
            print("fetched project:", project)
            if project is None:
                return Response(
                    {
                        "is_success": False,
                        "message": "Invalid Project Id",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            return Response(
                        {
                            "is_success": True,
                            "message": "Project details for project" + project.name,
                            "data": {
                                        "id": project_id,
                                        "name": project.name,
                                        "description": project.description,
                                        "start_date": project.start_date,
                                        "estimated_delivery_date": project.estimated_delivery_date
                                    }
                        },
                        status=status.HTTP_200_OK
                    )

        except Exception as Exc:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Creating Project ",
                    "data": Exc.__str__()
                },
                status = status.HTTP_200_OK
            )

    def post(self, request, format=None):
        if not request.user.is_authenticated:
                return Response(
                    {
                        "is_success": False,
                        "message": "user must login to access",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        data = request.data
        resp_data = Project.objects.create(
            name = data.get("name", None),
            description = data.get("description", None),
            start_date = data.get("start_date", None),
            estimated_delivery_date = data.get("estimated_delivery_date", None)
        )
        print("resp_data",resp_data)
        # user = User.objects.filter(id=request.user)
        mapping_resp_data = ProjectUserMapping.objects.create(
            project = resp_data,
            user = request.user,
            is_owner = True,
            is_active = True
        )
        print("mapping_resp_data",mapping_resp_data)
        return Response(
                {
                    "is_success":True,
                    "message": "Project Added Successfully",
                    "data": None
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request, format=None):
        try:
            project_id = request.query_params.get("project",None)
            if not project_id:
                return Response(
                    {
                        "is_success":False,
                        "message": "Task Id is missing",
                        "data": None
                    },
                    status=status.HTTP_200_OK,
                )
            project = Project.objects.filter(id__iexact=project_id)
            project.is_active = False
            project.save()
            return Response(
                {
                    "is_success":True,
                    "message": "Project Deleted Successfully",
                    "data": None
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {
                    "is_success":False,
                    "message": ex.__str__(),
                    "data": None
                },
                status=status.HTTP_200_OK,
            )
   