from django.contrib import admin
from django.urls import path
from occupations.views import OccupationsController

urlpatterns = [
    path('create', OccupationsController.as_view()),
    path('get', OccupationsController.as_view())
]
