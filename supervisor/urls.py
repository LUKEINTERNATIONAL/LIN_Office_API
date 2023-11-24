from django.contrib import admin
from django.urls import path
from supervisor.views import  SupervisorController

urlpatterns = [
    path('create', SupervisorController.as_view()),
    path('update', SupervisorController.as_view()),
    path('get', SupervisorController.as_view()),
    path('delete', SupervisorController.as_view())
]
