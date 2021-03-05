from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('login',views.loginUser),
    path('logout',views.logoutUser),
   
]