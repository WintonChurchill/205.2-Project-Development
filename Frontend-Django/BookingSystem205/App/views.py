from django.shortcuts import render
from django. template import loader 
from django.http import HttpResponse

#extra django libraries to complete forgot password / reset password feature ! 
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request): 
    return render(request, 'contact.html')

def LoginView(request): 
    return render(request, 'Login.html')

#Work in progress 31/10/25 - 02/10/25
def RegisterView(request): 
    #Incoming form submission collect user data 
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False 

    #Email Validation 
    if User.objects.filter(email=email).exists(): 
        user_data_has_error = True 
        messages.error(request, 'Email already exists')
    
    #Password Validation at least 8 characters long! 
    if len(password) < 8: 
        user_data_has_error = True 
        messages.error(request, 'Password must be at least 8 characters long!')

    #Create new user if no error and redirect to the Login page: 
    if not user_data_has_error: 
        new_user = User.objects.create_user(
            email = email, 
            password = password, 
        )
        messages.sucess(request, 'Account created. You can now Login')
        return redirect('Login')
    else: 
        return redirect('Register')
    

def Contact_form(request): 
    return render(request, 'Contact_form.html')

def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

