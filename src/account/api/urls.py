"""account URL Configuration

Add API endpoints urls here.
"""
from django.urls import path

from account.api import views

urlpatterns = [
    # user
    path('users/', views.UserListAPIView.as_view(), name=views.UserListAPIView.name),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name=views.UserDetailAPIView.name),
    path('users/register/', views.UserRegisterAPIView.as_view(), name=views.UserRegisterAPIView.name),
]
