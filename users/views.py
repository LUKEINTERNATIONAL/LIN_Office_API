from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView 
from users.custom_permissions import CustomPermissionMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import logging
from services.service import ApplicationService
from django.http import JsonResponse
from users.models import CustomUser
from users.serializer import RegisterRequestSerializer, PatchRequestSerializer, LoginSerializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login
from services.tasks import send_sms_email
from emails.views import EmailDetails
import random
import string
from django.http import JsonResponse

import json
logging.basicConfig(level=logging.INFO)   
service = ApplicationService()
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
config_data = json.load(open(os.path.join(BASE_DIR,'config.json')))   

class LoginAPIView(APIView): 
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                user = CustomUser.objects.get(username=username)
                return Response({
                    "message": "success", 
                    "code": status.HTTP_201_CREATED, 
                    "name": user.name,
                    "is_superuser": user.is_superuser,
                    "username": user.username,
                    "Token": token.key,
                    "id": user.id
                    })
            return Response(
                {"message": "error", "code": status.HTTP_401_UNAUTHORIZED, "details": ["Invalid credentials"]})
            
class UserView(CustomPermissionMixin,APIView):
    
    def get(self, request): # list user
        service = ApplicationService()
        if(request.user.is_superuser):
            query ='''SELECT cu.id,cu.is_superuser,cu.username,cu.email,
            cu.name, cu.phone, o.occupation_name,p.project_name
            FROM users_customuser cu
            LEFT JOIN project_user pu on pu.user_id = cu.id
            LEFT JOIN occupation_user ou on ou.user_id = cu.id
            LEFT JOIN projects p on p.id = pu.project_id
            LEFT JOIN occupations o on o.id = ou.occupation_id
            '''
        elif(request.user.zone_id is not 0):
             query ='''SELECT * FROM users_customuser 
            '''
        else:
             query ='''SELECT * FROM users_customuser 
            '''.format(request.user.id)
        results = service.query_processor(query)
        return JsonResponse({
            'users':results
        })
    
    def generate_random_password(self, length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    
    def post(self, request):
        data = request.data  
        # try:
        #     data = request.data  
        # except AttributeError:
        #     data = request
        # serializer = RegisterRequestSerializer(data=data)
        # if not serializer.is_valid():
        #     logging.warning(f"attempt register: Format Error")
        #     return Response({"status": "Format Error"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        # data = serializer.validated_data
        try:
            user = CustomUser.objects.get(username=data["username"])
            logging.warning(f"attempt register: Username Existed")
            return Response({"status": "Username Existed"}, status=status.HTTP_409_CONFLICT)
        except ObjectDoesNotExist:
            pass

        password =self.generate_random_password()
        CustomUser.objects.create_user(
            username=data["username"],
            password=password,
            email=data["email"], 
            name=data["name"],
            birthdate=data["birthdate"],
            occupation=data["occupation"],
            phone=data["phone"],
            is_superuser=data["is_superuser"],
        )
        message = EmailDetails().compose_password_email(data["name"], data["username"],password)
        EmailDetails().send_email(data["email"],message,'Your New Account has been Created!')
        return Response({"status": "OK"})
    
    def put(self, request):
        try:
            user = CustomUser.objects.get(id=request.data['id'])
        except ObjectDoesNotExist:
            return Response({"status": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        user.username = request.data['username']
        user.email = request.data['email']
        user.name = request.data['name']
        user.birthdate = request.data['birthdate']
        user.occupation = request.data['occupation']
        user.phone = request.data['phone']
        user.is_superuser = request.data['is_superuser']
        user.save()
        return Response({"status": "OK"})
    
    def delete(self, request, pk):
        
        try:
            user = CustomUser.objects.get(id=pk)
        except ObjectDoesNotExist:
            logging.warning(f"attempt delete: Username Not Found")
            return Response({"status": "Username Not Found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            user.delete()
            return Response({"status": "OK"})
        except:
            logging.error(f"attempt delete {pk}: server error")
            return Response({"status": "Username Not Found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HisOfficer(CustomPermissionMixin,APIView):
    def get(self, request): # list user
        service = ApplicationService()
        query ='''SELECT * FROM users_customuser u 
        LEFT JOIN facilities f on f.district_id = u.district_id
        WHERE f.id = {}
        '''.format(request.GET['facility_id'])
        results = service.query_processor(query)
        return JsonResponse({
            'users':results
        })
class SingleUserView(CustomPermissionMixin,APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            logging.warning(f"attempt get: Username Not Found")
            return Response({"status": "Username Not Found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"username": user.username, "email": user.email, "is_staff": user.is_staff, 
                            "is_superuser": user.is_superuser})

    def patch(self, request, username):
       
        try:
            data = request.data  
        except AttributeError:
            data = request
        
        serializer = PatchRequestSerializer(data=data)
        if not serializer.is_valid():
            logging.warning(f"attempt patch user: Format Error")
            return Response({"status": "Format Error"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if username != data["username"]:
            logging.warning(f"attempt patch user: Username Not Match {username} {data['username']}")
            return Response({"status": "Format Error"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        data = serializer.validated_data
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            logging.warning(f"attempt patch user: Username Not Found {username}")
            return Response({"status": "Username Not Found"}, status=status.HTTP_404_NOT_FOUND)
       
        
        if "email" in data:
            user.email = data["email"]
        user.is_staff = data["is_staff"]
        user.is_superuser = data["is_superuser"]
        user.save()
        
        return Response({"status": "OK"})

    