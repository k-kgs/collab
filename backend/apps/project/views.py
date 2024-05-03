import os
from django.shortcuts import render

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
        if not request.user.is_authenticated:
            return Response(
                {
                    "is_success": False,
                    "message": "user must login to access",
                    "data": None
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(
                    {
                        "is_success": True,
                        "message": "Task list for " + request.user.email,
                        "data": {
                            "my_project": [
                                {
                                    "id": 1,
                                    "name": "project1"
                                },
                                {
                                    "id": 2,
                                    "name": "project2"
                                }
                            ],
                            "shared_project": [
                                {
                                    "id": 3,
                                    "name": "project3"
                                },
                                {
                                    "id": 4,
                                    "name": "project4"
                                }
                            ]
                        }
                    },
                    status=status.HTTP_200_OK
                )