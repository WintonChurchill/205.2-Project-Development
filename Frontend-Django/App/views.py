from django.shortcuts import render, redirect
from django. template import loader 
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime, timedelta
import requests
from django.contrib.auth.decorators import login_required


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
    

@login_required
def booking_view(request):
    flask_base = settings.FLASK_API_URL

    start_day = datetime.now().replace(hour=9, minute=0)
    end_day = datetime.now().replace(hour=17, minute=0)

    time_slots = []
    current = start_day

    while current < end_day:
        next_slot = current + timedelta(minutes=30)

        response = requests.get(
            f"{flask_base}/api/bookings",
            params={"start_time": current.isoformat(), "end_time": next_slot.isoformat()}
        )

        booked = False
        user_email = None
        if response.status_code == 200 and response.json():
            booked = True
            user_email = response.json()[0]['user']

        time_slots.append({
            "start_time": current,
            "end_time": next_slot,
            "booked": booked,
            "user_email": user_email
        })

        current = next_slot

    if request.method == "POST":
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        user_id = request.user.id

        post_response = requests.post(
            f"{flask_base}/api/bookings",
            json={"start_time": start_time, "end_time": end_time, "user_id": user_id}
        )

        if post_response.status_code == 201:
            return redirect("booking")
        else:
            error = post_response.json().get("error", "Booking failed")
            return render(request, "booking.html", {"time_slots": time_slots, "error": error})

    return render(request, "booking.html", {"time_slots": time_slots})