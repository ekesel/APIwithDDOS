from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializers import *
# Create your views here.
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from .models import *
from ratelimit.decorators import ratelimit

@api_view(['POST',])
@permission_classes((AllowAny, ))
def mylogin(request):
    if request.method == "POST":
        serializer = loginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                match=User.objects.get(email=email)
                if match.email == email and check_password(password,match.password) == True:
                    # user = authenticate(email=email, password=password)
                    # print(user)
                    # if user is not None:
                    login(request, match)
                    data['email'] = match.email
                    data['success'] = "Successfully Logged In!"
                    return Response(data,status=200)
                else:
                    data['error'] = {}
                    data['error']['message'] = "check your mail id or password entered"
                    data['error']['description'] = "Incorrect mail id and password"
                    return Response(data,status=400)
            except User.DoesNotExist:
                data['error'] = {}
                data['error']['message']="User not found"
                data['error']['description'] = "User does not exists"
                return Response(data,status=404)
        else:
            data = serializer.errors
            return Response(data,status=406)


@api_view(['POST',])
@permission_classes((AllowAny, ))
@ratelimit(key='ip', rate='5/m')
def upload(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        data = {'Error':'too many attempts'}
        return Response(data,status=429)
    if request.method == 'POST':
        user = request.user
        if user.id == None:
            data = {'Error':'Not logged in'}
            return Response(data,status=403)
        serializer = FileSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            files = serializer.validated_data['files']
            obj = uploaded.objects.create(user=user,files=files)
            data['id'] = obj.id
            return Response(data,status=200)
        else:
            data = serializer.errors
            return Response(data,status=406) 
        
