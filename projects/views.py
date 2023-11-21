from django.shortcuts import render
from users.custom_permissions import CustomPermissionMixin
from rest_framework.views import APIView 
from rest_framework.response import Response
from projects.serializer import ProjectsSerializer
from django.http import JsonResponse
from projects.models import Projects


# Create your views here.
class CreateProject(CustomPermissionMixin,APIView):
    def post(self,request):
        try:
            data = request.data  
        except AttributeError:
            data = request
        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
        

class List(CustomPermissionMixin, APIView):
    def get(self, request):
        projects_queryset = Projects.objects.all()
        serializer = ProjectsSerializer(projects_queryset, many=True)
        return Response({'projects': serializer.data})
