from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Reservation
from .forms import ReservationForm
from datetime import date
from datetime import timedelta


def index(request):
    return render(request, 'hotel/index.html')
def home(request):
    return render(request, 'hotel/home.html')
def register(request):
    return render(request, 'hotel/register.html')
def loginPage(request):
    return render(request, 'hotel/login.html')
def base(request):
    return render(request, 'hotel/base.html')
def makereservation(request):
    return render(request, 'hotel/makereservation.html')
def reserve(request):
    return render(request, 'hotel/reserve1.html')
def update_reservation(request):
        return render(request, 'hotel/reserve1.html')
def chat(request):
    return render (request, 'hotel/chat.html')

def available(request):
    available_rooms = Room.objects.filter(is_available=True)
    reserved_rooms = Reservation.objects.filter(status='Booked')

    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        room = available_rooms.filter(room_number=room_number).first()

        if room:
            room.is_available = False
            room.save()

            Reservation.objects.create(
                room_number=room.room_number,
                room_type=room.room_type,
                check_in=None,  
                check_out=None,  
                status='Booked'
            )

            return redirect('available')

    context = {
        'available_rooms': available_rooms,
        'reserved_rooms': reserved_rooms
    }
    return render(request, 'hotel/availability.html', context)

def update(request):
    q = request.user
    context={
        "Reservations": Reservation.objects.filter(user = q)
    }
    return render(request, 'hotel/update1.html', context)

def cancel(request):
    q = request.user
    context={
        "Reservations": Reservation.objects.filter(user = q)
    }
    return render(request, 'hotel/cancel1.html', context)

def reservation(request):
    q = request.user
    context={
        "Reservations": Reservation.objects.filter(user = q)
    }
    return render(request, 'hotel/reservation.html', context)


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            reservation = form.save()
            return redirect('../reservation1', pk=reservation.pk)
    else:
        form = ReservationForm(initial={'user': request.user})
    return render(request, 'hotel/reserve1.html', {'form': form})

def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation1')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'hotel/reserve1.html', {'form': form, 'reservation': reservation})

def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('reservation1')
    return render(request, 'hotel/reservation.html', {'reservation': reservation})

def register (request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('../login')
        else:
            print(form.errors)   
    context_dictionary = {'form': form}
    return render(request, 'hotel/register.html', context_dictionary)

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password2')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect (home)
        else:
            messages.info(request, 'Username or password incorrect')
    context = {}
    return render(request, 'hotel/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect(loginPage)

def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = User.objects.get(username='bilalattahiru') 
            message.save()
            return redirect('inbox1')
    else:
        form = MessageForm()
    return render(request, 'hotel/chat.html', {'form': form})

def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'hotel/inbox.html', {'messages': messages})

def extra(request):
    return render(request, 'hotel/services.html')

def bookservice(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect(bookedservice)
    else:
        form = ServiceForm(initial={'user': request.user})
    return render(request, 'hotel/bookservice.html', {'form': form})

def bookedservice(request):
    context={
        "Services": Service.objects.filter(user = request.user)
    }
    return render(request, 'hotel/bookedservices.html', context)
