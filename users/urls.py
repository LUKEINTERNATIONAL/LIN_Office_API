from django.urls import path
from users.views import  UserView, SingleUserView, LoginAPIView,HisOfficer

urlpatterns = [
    path('list', UserView.as_view()),
    path('his_officer', HisOfficer.as_view()),
    path('update', UserView.as_view()),
    path('create', UserView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('<str:username>', SingleUserView.as_view())
]
