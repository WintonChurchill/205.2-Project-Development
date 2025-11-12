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

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import render, request

#Clean up files as well / commenting etc..

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

#IMPORTANT NOTICE: due to I had tested our project via a new register system outside of this project, 
#I will be completing the rest of the copying of the new files, modifying and completed by tomorrow during class time 
#Only part left is to test everything in new project and also forgot password feature 
#will provide screenshots proof work completed for testin on 12/11/25

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
            messages.success(request, 'Account created succesfully!')
            return redirect('login')
        else: 
            return redirect('register')

    return render(request, 'register.html')

    return render(request, 'register1.html')

#new login page - working! (need to test tomorrow during class time)
def LoginView(request): 
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)

            return redirect('home')
        else: 
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'Login.html')

#completed and working
def LogoutView(request): 
    logout(request)

    return redirect('login')



def signup(request): 
    return redirect(request, 'signup.html')

def contact(request): 
    return render(request, 'contact.html')

def LoginView(request): 
    if request.method == 'POST': 
        #collect user input from front-end
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

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
#Complete
def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

