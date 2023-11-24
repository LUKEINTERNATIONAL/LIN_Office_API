from django.shortcuts import render
from users.custom_permissions import CustomPermissionMixin
from rest_framework.views import APIView 
from rest_framework.response import Response
from occupations.serializer import OccupationSerializer
from django.http import JsonResponse
from occupations.models import Occupations
from rest_framework import status
from services.service import ApplicationService
import json

class OccupationsController(CustomPermissionMixin, APIView):
    def post(self,request):
        try:
            data = request.data  
        except AttributeError:
            data = request
        serializer = OccupationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
    def get(self, request):
        service = ApplicationService()
        query ='''SELECT * from occupations'''
        results = service.query_processor(query)
        return JsonResponse({
            'occupations':results
        })
        
    def put(self, request):
        timesheet = Occupations.objects.get(pk=request.data['id'])
        serializer = OccupationSerializer(timesheet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
