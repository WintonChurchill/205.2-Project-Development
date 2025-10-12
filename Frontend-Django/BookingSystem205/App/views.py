from django.shortcuts import render
from django. template import loader 
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def Contact(request): 
    return render(request, 'Contact.html')

def Login(request): 
    return render(request, 'Login.html')

def Register(request): 
    return render(request, 'Register.html')

def Contact_form(request): 
    return render(request, 'Contact_form.html')

def About_us(request): 
    return render(request, 'About_us.html')
