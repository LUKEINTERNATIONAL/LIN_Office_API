from django.contrib import admin
from django.urls import path
from timesheets.views import  TimesheetController

urlpatterns = [
    path('create', TimesheetController.as_view()),
    path('update', TimesheetController.as_view()),
    path('get', TimesheetController.as_view()),
    path('delete', TimesheetController.as_view())
]
