from django.shortcuts import render
from django.http import HttpResponse

# This is where you do any render requests -> rendering webpages (html files)

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request, "booking.html")

def contact(request):
    return render(request, "contact.html")



