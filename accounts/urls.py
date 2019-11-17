from django.urls import path, include
# from django import HttpResonse, redirect
from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register', views.register, name= 'register'),
    path('change_password', views.change_password, name='password_change')# path('login', views.login, name='login'),
]
