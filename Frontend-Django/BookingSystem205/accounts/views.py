from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  
from django.views.generic import CreateView
from django_password_eye.fields import PasswordEye 
from django_password_eye.widgets import PasswordEyeWidget

#Register Form Views(1
class SignUpView(CreateView): 
   form_class = UserCreationForm       
   success_url = reverse_lazy('login')   
   template_name = "registration/signup.html" 
   
   #Add Email replacement of username and password 

#Forgot Password View 

