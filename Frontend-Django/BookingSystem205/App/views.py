from django.shortcuts import render
from django. template import loader 
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.conf import settings 
from django.core.mail import EmailMessage 
from django.utils import timezone 
from django.urls import reverse 
from .models import * 

#extra django libraries to complete forgot password / reset password feature ! 
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django.views import View

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request): 
    return render(request, 'contact.html')

def LoginView(request): 
    return render(request, 'Login.html')


def RegisterView(request): 
    if request.method =='POST': 
        #collect user inputs 
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False 

        #check if email not being used
        if User.objects.filter(email=email).exists(): 
            user_data_has_error = True 
            messages.error(request, 'Email already exists')

        #password validation 
        if len(password) < 8: 
            user_data_has_error = True 
            messages.error(request, 'Password must be at least 8 characters long')

        if not user_data_has_error: 
            new_user = User.objects.create_user(
                email = email, 
                password = password
            )
            messages.success(request, 'Account created. Login Now!')
            return redirect('Login.html')
        else: 
            return HttpResponse(request, 'Register.html')

    

def Contact_form(request): 
    return render(request, 'Contact_form.html')

def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

