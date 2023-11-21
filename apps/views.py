from django.shortcuts import render
from users.custom_permissions import CustomPermissionMixin
from rest_framework.views import APIView 
from rest_framework.response import Response
from apps.serializer import AppSerializer
from django.http import JsonResponse
from apps.models import Apps


# Create your views here.
class CreateApp(CustomPermissionMixin,APIView):
    def post(self,request):
        try:
            data = request.data  
        except AttributeError:
            data = request
        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

class ListApps(CustomPermissionMixin, APIView):
    def get(self, request):
        apps_queryset = Apps.objects.all()
        serializer = AppSerializer(apps_queryset, many=True)
        return Response({'apps': serializer.data})
