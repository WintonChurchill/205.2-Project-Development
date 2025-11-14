from django.template import loader 
from django.http import HttpResponse #representing an import of HttpResponse class -  

from django.shortcuts import render, redirect 
#render -return an HttpResponse object that redners text 
# redirect - returns  HttpResponseRedirect to appropriate URL for aguments to be passed

from django.contrib.auth.models import User #built-in authentication
from django.contrib.auth import authenticate, login, logout#django built-in authentication system (essential functions)
from django.contrib.auth.decorators import login_required#imports a decorator which enables an barrier for users to not having access to other pages
from django.contrib import messages #display one time notification messages to users e.g upon succesful account creation, invalid credentials
from django.conf import settings #standard method to access BookingSystem205 project configuration settings*
from django.core.mail import EmailMessage#sending emails via django apps / Not implemeneted
from django.utils import timezone#current timezone for password Id not implemented!
from django.urls import reverse
from .models import * #django database library that 

#User must login/register first then redirect them once succesfully logged in!
@login_required 
def home(request):
    return render(request, 'home.html')

#new Register page - working (edit and final test tomorrow during class time!)
def RegisterView(request): 
    if request.method == 'POST': 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #Flag Error 
        user_data_has_error = False 

        #Username validation check if exists or Not
        if User.objects.filter(username=username).exists():
            user_data_has_error = True 
            messages.error(request, 'Username already exists')

        #Email validation check if exists or Not
        if User.objects.filter(email=email).exists():
            user_data_has_error = True 
            messages.error(request, 'Email already exists')

        #Password validation
        if len(password) < 5: 
            user_data_has_error = True
            messages.error(request, 'Password must be at least 5 characters')

        #create a new user if user input is correct! 
        if not user_data_has_error:
            new_user = User.objects.create_user(
                username = username, 
                email = email, 
                password = password
            )
            messages.success(request, 'Account created succesfully!')#flash message for successful login attempt
            return redirect('login')#redirect to login.html file
        else: 
            return redirect('register')#redirect to register.html file

    return render(request, 'register1.html')#return 'register1.html' file

#new login page - working! (need to test tomorrow during class time)
def LoginView(request): 
    #collect user input from form (username + password)
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get('password')

        #user authentication (request - collect username, password)
        user = authenticate(request, username=username, password=password)

        #if user credentials is correct based of registered user credentials redirect to home
        if user is not None: 
            login(request, user)

            return redirect('home')
        else: #if not: user will remain on login page (flash message appears)!
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'login1.html')#return 'login.html'file

#Logout Feature
def LogoutView(request): 
    
    logout(request)

    return redirect('login')#redirect to login1.html file

#Contact Page
def contact(request): 
    return render(request, 'contact.html')#contact page redirect 

#About us page
def about(request): 
    return render(request, 'about.html')

#Booking page
def booking(request): 
    return render(request, 'booking.html')

