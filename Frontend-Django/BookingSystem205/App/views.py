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

def RegisterView(request): 
    if request.method == "POST": 
        #collect user inputs 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False 

        #Username validation 

        if User.objects.filter(username=username).exists(): 
            user_data_has_error = True 
            messages.error(request, 'Username already exists!')

        #check if email not being used
        if User.objects.filter(email=email).exists(): 
            user_data_has_error = True 
            messages.error(request, 'Email already exists')

        #password validation 
        if len(password) < 14: 
            user_data_has_error = True 
            messages.error(request, 'Password must be at least 8 characters long')

        if not user_data_has_error: 
            new_user = User.objects.create_user(
                username = username,
                email=email,
                password=password
            )
            user = authenticate(request=request, userame=username, email=email,password=password)
            messages.success(request, 'Account created. Login Now!')
            return redirect('login')
        
    return render(request, 'register.html')
    
#In-progress (03/11/25)
def LoginView(request): 
    if request.method == 'POST': 
        #collect user input from front-end
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None: 
            login(request, user)

            return redirect('Home')
    
        else: 
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'Login.html')


#Incomplete
def LogoutView(request): 
    logout(request)
    return redirect('login')

#Incomplete
def ForgotPassword(request): 
    return render(request, 'forgot_password.html')

#Incomplete
def PasswordResetSent(request, reset_id): 
    return redirect('fogot-password')

#Incomplete
def ResetPassword(request, reset_id): 
    return redirect('reset-password', reset_id=reset_id)

#Complete
def Contact_form(request): 
    return render(request, 'Contact_form.html')

#Complete
def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

