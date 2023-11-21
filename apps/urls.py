from django.contrib import admin
from django.urls import path
from apps.views import CreateApp, ListApps

urlpatterns = [
    path('create_app', CreateApp.as_view()),
    path('list', ListApps.as_view())
]
