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
            messages.success(request, 'Account created succesfully!')
            return redirect('login')
        else: 
            return redirect('register')

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

    return render(request, 'login1.html')

#completed and working
def LogoutView(request): 
    logout(request)

    return redirect('login')



def contact(request): 
    return render(request, 'contact.html')

#completed - Login view
def LoginView(request): 
    if request.method == 'POST': 
        #collect user input from front-end
        username = request.POST.get('username')
        password = request.POST.get('password')

        #user authentication
        user = authenticate(request, username=username, password=password)

        #if user credentials are existing, user will be redirected to 'home' page
        if user is not None: 
            login(request, user)

            return redirect('home')

        #if user credentials are not existing an invalid login credentials will show via (flash messages)
        else: 
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'Login1.html')


def LogoutView(request): 
    logout(request)
    return redirect('login')

#Not-functional
def ForgotPassword(request): 

    if request.method == "POST":
        email = request.POST.get('email')

        try: 
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            messages.success(request, f"Email found!")
            
            email_body = f'Reset your password using the link below: \n\n\n{password_reset_url}',

            email_message = EmailMessage(
                'Reset your password', #email subject
                email_body,
                settings.EMAIL_HOST_USER, #email sender
                [email]#email receiver
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist: 
            messages.error(request, f"No user with email '{email}' found")
            return redirect('forgot-password')
        
    return render(request, 'forgot_password.html')
        
#In-progress
def PasswordResetSent(request, reset_id): 
    
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request,'password_reset_sent.html')
    else: 
        #redirect to forgot password page if code doe not exist! 
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

#Incomplete
def ResetPassword(request, reset_id): 
 
        if request.method == "POST": 
            password = request.POST.get('password')
            confirm_password = request.POST.get('conrfirm_password')

            passwords_have_error = False

            if password != confirm_password: 
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')

            if len(password) < 5: 
                passwords_have_error = True 
                messages.error(request, "Password must be at least 5 characters long")

            expiration_time = reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time: 
                
                reset_id.delete()

                passwords_have_error = True
                messages.error(request, 'Reset link has expired')

            if not passwords_have_error: 
                user = reset_id.user
                user.set_password(password)
                user.save()

                reset_id.delete()

                messages.success(request, 'Password reset, proceed to login')
                return redirect('login')
            else:
                #redirect back to password reset page and display errors 
                return redirect('reset-password', reset_id=reset_id)

    #  return render(request, 'reset_password.html' )

#Complete
def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')

def main(request): 
    return render(request, 'main.html')

