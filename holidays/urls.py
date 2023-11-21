from django.contrib import admin
from django.urls import path
from holidays.views import CreateHoliday, List

urlpatterns = [
    path('create', CreateHoliday.as_view()),
    path('list', List.as_view())
]
