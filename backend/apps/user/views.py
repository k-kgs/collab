import os
from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from .models import User



# Create your views here.

class HealthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            return Response(
                {
                    "is_success": True,
                    "message": "User Health is UP",
                    "data": None
                },
                status = status.HTTP_200_OK
            )
        except Exception as ex:
            return Response(
                {
                    "is_success": False,
                    "message": "Caught Exception While Checking User Health",
                    "data": None
                },
                status = status.HTTP_200_OK
            )
        
class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            print("request received:",request.data)
            is_success = False
            message = "Bad Request"
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(
                        {
                            "is_success": True,
                            "message": "User Registered Successfully",
                            "data": serializer.data
                        },
                        status= status.HTTP_201_CREATED
                    )
                
                except Exception as ex:
                    return Response(
                        {
                            "is_success": False,
                            "message": "Caught Exception While Registering User",
                            "data": None
                        },
                        status = status.HTTP_500_INTERNAL_SERVER_ERROR
                    )   
            return Response(
                {
                    "is_success": False,
                    "message": "Invalid Request",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )            
        
        except Exception as ex:
            print("Exception while registering user:",ex.__str__())
            return Response(
                {
                    "is_success": False,
                    "message": "Unable To Register User at the Moment",
                    "data": None
                },
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserLogin(APIView):
    def post(self, request, format=None):
        print("request received", (request.data))
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'payload':{'token': token.key}}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserDetails(APIView):
    def get(self, request, format=None):
        print("request received",request)
        if not request.user.is_authenticated:
            return Response(
                {
                    "is_success": False,
                    "message": "user must login to access",
                    "data": None
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        user = request.user
        return Response(
                    {
                        "is_success": True,
                        "message": "user details for " + request.user.email,
                        "data": {
                            "username": str(user)
                        }
                    },
                    status=status.HTTP_200_OK
                )