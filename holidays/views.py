from django.shortcuts import render
from users.custom_permissions import CustomPermissionMixin
from rest_framework.views import APIView 
from rest_framework.response import Response
from holidays.serializer import HolidaySerializer
from django.http import JsonResponse
from holidays.models import Holidays


# Create your views here.
class CreateHoliday(CustomPermissionMixin,APIView):
    def post(self,request):
        try:
            data = request.data  
        except AttributeError:
            data = request
        serializer = HolidaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

class List(CustomPermissionMixin, APIView):
    def get(self, request):
        queryset = Holidays.objects.all()
        serializer = HolidaySerializer(queryset, many=True)
        return Response({'holidays': serializer.data})
