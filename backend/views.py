# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Location,DroneShot,Customer,Booking
from .forms import LocationForm,DroneForm,BookingForm
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            cust=Customer(request.user.id)
            cust.save()
            return redirect('home')
    else:
        form = UserCreationForm()
        # return HttpResponse("Hello")
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'home.html', context)

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LocationForm()
        # return HttpResponse("Hello")
    return render(request, 'add_location.html', {'form': form})

def delete_location(request, location_id):
    location = Location.objects.get(id=location_id)
    location.delete()
    return redirect('home')



def drone(request, location_id):
    # Retrieve the Location object for the given ID
    location = Location.objects.get(pk=location_id)
    # Render the Drone template with the Location object as context
    return render(request, 'drone.html', {'location': location})


def add_drone(request):
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DroneForm()
    return render(request, 'add_drone.html', {'form': form})


def book_drone(request, location_id):
    location = Location.objects.get(pk=location_id)
    drones = DroneShot.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            customer =Customer.objects.get(user_id=request.user.id)
            booking.customer = customer
            booking.location = location
            booking.save()
            return HttpResponse("Drone booked")
    else:
        form = BookingForm()

    context = {
        'location': location,
        'drones': drones,
        'form': form,
    }
    return render(request, 'book_drone.html', context)


def view_bookings(request):
    bookings = Booking.objects.filter(customer=Customer.objects.get(user_id = request.user.id))
    context = {'bookings':bookings}
    return render(request, 'view_bookings.html', context)

#delete the booking can be only done by admin
def delete_booking(request, booking_id):
    # Retrieve the booking record based on the booking ID
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.user.is_staff:
        # Delete the booking record
        booking.delete()

        # Redirect to the booking list page
        return redirect(reverse('view_bookings'))
    else :
        message = "you are not allowed to delete the booking"
        return HttpResponse(message)
