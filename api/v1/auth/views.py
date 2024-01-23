import requests
import json

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    email = request.data["email"]
    password = request.data["password"]
    name = request.data["username"]
    # profile_picture = request.data["profile_picture"]
    # phone_number = request.data["phone_number"]
    # age = request.data["age"]
    

    if not (email and password):
        response_data = {
            "status" : 6001,
            "message" : "Both username and password are required. !!!"
        } 
        return Response(response_data)
    
    # try:
    #     validate_password(password)
    # except ValidationError as e:
    #     response_data = {
    #         "status": 6005,
    #         "data": None,
    #         "message": f"Password validation error: {', '.join(e.messages)}",
    #     }
    #     return Response(response_data, status=400)

    if not User.objects.filter(username = name).exists():
        user = User.objects.create_user(
            username = name,
            email = email, 
            password = password,
        )
        # Profile.objects.create(user=user,name =name,email =email,profile_picture = profile_picture, phone_number=phone_number, age=age)

        data = {  "username" : email, "password" : password }
        url = "http://127.0.0.1:8000/api/v1/auth/token/"
        headers = {
            "Content-Type" : "application/json"      
        }
        response = requests.post(url, headers=headers, data = json.dumps(data))
        print(response)

        response_data = {
            "status" : 6000,
            "data" : response.json(),
            "message" : "User Created Successfully"
        } 

    else :
        response_data = {
            "status" : 6001,
            "data" : "Error Occured",
            "message" : "User already exists !!!"
        } 
    return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not (username and password):
        response_data = {
            "status" : 6001,
            "message" : "Both username and password are required. !!!"
        } 
        return Response(response_data)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response_data = {
            "status" : 6001,
            "message" : "Invalid username. !!!"
        } 
        return Response(response_data)

    if not user.check_password(password):
        response_data = {
            "status" : 6001,
            "message" : "Invalid password. !!!"
        } 
        return Response(response_data)
    context={
            "request" : request,
        }
    
    data = {  "username" : username, "password" : password }
    url = "http://127.0.0.1:8000/api/v1/auth/token/"
    headers = {
        "Content-Type" : "application/json"      
    }
    response = requests.post(url, headers=headers, data = json.dumps(data))
    print(response)

    response_data = {
        "status" : 6000,
        "data" : response.json(),
        "message" : "Logged In Successfully"
    } 
    return Response(response_data)