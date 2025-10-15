from django.shortcuts import render
from django. template import loader 
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request): 
    return render(request, 'contact.html')

def Login(request): 
    return render(request, 'Login.html')

def Register(request): 
    return render(request, 'Register.html')

def Contact_form(request): 
    return render(request, 'Contact_form.html')

def about(request): 
    return render(request, 'about.html')

def booking(request): 
    return render(request, 'booking.html')
    

