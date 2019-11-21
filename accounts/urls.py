from django.urls import path, include
# from django import HttpResonse, redirect
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='templates/registration/password_change_form.html'),),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register', views.register, name= 'register'),
]
