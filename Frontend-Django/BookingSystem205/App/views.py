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

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request): 
    return redirect(request, 'signup.html')

def contact(request): 
    return render(request, 'contact.html')

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
#Complete
def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

