from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  
from django.views.generic import CreateView
from django_password_eye.fields import PasswordEye 
from django_password_eye.widgets import PasswordEyeWidget
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



   #Add Email replacement of username and password 

#Forgot Password View 

