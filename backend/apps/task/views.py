import os
from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class TaskView(APIView):
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
                            "my_task": [
                                {
                                    "id": 1,
                                    "name": "task1"
                                },
                                {
                                    "id": 2,
                                    "name": "task2"
                                }
                            ]
                        }
                    },
                    status=status.HTTP_200_OK
                )