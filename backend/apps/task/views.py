import os
from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from apps.project.models import Project

class TaskListView(APIView):
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
            project_id =  request.query_params.get('project_id', None)
            project = Project.objects.filter(id=project_id).first()
            project_task = Task.objects.filter(
                project = project,
                is_active = True
            )
            task_list = list()
            for item in project_task:
                task_list.append(
                    {
                        "id": item.id,
                        "name": item.name,
                        "status": item.status,
                        "description": item.description,
                    }
                )
            return Response(
                    {
                        "is_success": True,
                        "message": "Task list for project: " + project.name,
                        "data": task_list
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as Exc:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Getting Task ",
                    "data": Exc.__str__()
                },
                status = status.HTTP_200_OK
            )

class TaskView(APIView):
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
            task_id =  request.query_params.get('task', None)
            print("task_id",task_id)
            if task_id is None:
                return Response(
                    {
                        "is_success": False,
                        "message": "Invalid Project Id",
                        "data": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            task = Task.objects.filter(id=task_id).first()
            print("fetched project:", task)
            if task is None:
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
                            "message": "Task details for project" + task.name,
                            "data": {
                                        "id": task_id,
                                        "name": task.name,
                                        "description": task.description,
                                        "status": task.status
                                    }
                        },
                        status=status.HTTP_200_OK
                    )

    
        except Exception as Exc:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Getting Task ",
                    "data": Exc.__str__()
                },
                status = status.HTTP_200_OK
            )

    def post(self, request, format=None):
        try:
            data = request.data
            project_id = data.get("project_id",None)
            project = Project.objects.filter(id=project_id).first()
            task_status = Task.Status.TODO
            resp_data = Task.objects.create(
                project = project,
                name = data.get("name", None),
                status = task_status,
                description = data.get("description", None)
            )
            return Response(
                {
                    "is_success":True,
                    "message": "Task Added Successfully",
                    "data": None
                },
                status=status.HTTP_200_OK,
            )
        except Exception as Exc:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Creating Task ",
                    "data": Exc.__str__()
                },
                status = status.HTTP_200_OK
            ) 
    def delete(self, request, format=None):
        try:
            task_id = request.query_params.get("id",None)
            if not task_id:
                return Response(
                    {
                        "is_success":False,
                        "message": "Task Id is missing",
                        "data": None
                    },
                    status=status.HTTP_200_OK,
                )
            task = Task.objects.filter(id__iexact=task_id)
            task.is_active = False
            task.save()
            return Response(
                {
                    "is_success":True,
                    "message": "Task Deleted Successfully",
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
        
