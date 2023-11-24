from django.contrib import admin
from django.urls import path
from projects.views import CreateProject, List

urlpatterns = [
    path('create', CreateProject.as_view()),
    path('get', List.as_view())
]
