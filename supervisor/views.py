from django.shortcuts import render
from users.custom_permissions import CustomPermissionMixin
from rest_framework.views import APIView 
from rest_framework.response import Response
from timesheets.serializer import TimesheetSerializer
from django.http import JsonResponse
from timesheets.models import Timesheet
from rest_framework import status
from services.service import ApplicationService
import json
       
class SupervisorController(CustomPermissionMixin, APIView):
    def post(self,request):
        try:
            data = request.data  
        except AttributeError:
            data = request
        serializer = TimesheetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
    def get(self, request):
        service = ApplicationService()
        query ='''SELECT t.id,timesheet_date,task,description,t.holiday_id,t.project_id,t.user_id,
        start_time,end_time,project_name,holiday_name,t.status,t.attachments_id FROM timesheet t 
        INNER JOIN projects p on t.project_id = p.id 
        LEFT JOIN holidays h on t.holiday_id = h.id
        LEFT JOIN users_customuser u on t.user_id = u.id
        LEFT JOIN attachments a on t.attachments_id = a.id 
        WHERE t.timesheet_date BETWEEN '{}' AND '{}'
        AND u.id = '{}'
        order by timesheet_date desc'''.format(request.GET['start_date'],request.GET['end_date'],request.GET['user_id'])
        results = service.query_processor(query)
        return JsonResponse({
            'timesheet':results
        })
        
    def put(self, request):
        timesheet = Timesheet.objects.get(pk=request.data['id'])
        serializer = TimesheetSerializer(timesheet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self,request):
        timesheet = Timesheet.objects.get(pk=request.data['id'])
        timesheet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
