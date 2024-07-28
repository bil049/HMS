from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from .models import Reservation
from .forms import ReservationForm
from datetime import date
from datetime import timedelta



def admin_dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            auth.login(request, user)
            return redirect("room")  
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'hoteladmin/login.html')

@login_required
def register (request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('users')
        else:
            print(form.errors)   
    context_dictionary = {'form': form}
    return render(request, 'hoteladmin/usercreation.html', context_dictionary)

@login_required
def updateuser(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = CreateUserForm(instance=user)
    return render(request, 'hoteladmin/usercreation.html', {'form': form, 'user': user})

@login_required
def canceluser(request, pk):
    reservation = get_object_or_404(User, pk=pk)
    reservation.delete()
    return redirect('users')

@login_required
def users(request):
    context={
        "Users": User.objects.all()
    }
    return render(request, 'hoteladmin/users.html', context)

@login_required
def room(request):
    return render(request, 'hoteladmin/room.html')

@login_required
def manage_room(request):
    context={
        "Rooms": Room.objects.all()
    }
    return render(request, 'hoteladmin/viewroom.html', context)

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room.is_available = True
            form.save()
            return redirect('rooms')
    else:
        form = RoomForm()
    return render(request, 'hoteladmin/createroom.html', {'form': form})

@login_required
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = RoomForm(instance=room)
    return render(request, 'hoteladmin/createroom.html', {'form': form, 'room': room})

@login_required
def cancel_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('rooms')

@login_required
def updateroom(request):
    context={
        "Rooms": Room.objects.all()
    }
    return render(request, 'hoteladmin/updateroom.html', context)

@login_required
def cancelroom(request):
    context={
        "Rooms": Room.objects.all()
    }
    return render(request, 'hoteladmin/cancelroom.html', context)

@login_required
def reservation(request):
    return render(request, 'hoteladmin/reservation.html')

@login_required
def viewreservation(request):
    context={
        "Reservations": Reservation.objects.all()
    }
    return render(request, 'hoteladmin/viewreservation.html', context)

@login_required
def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            reservation = form.save()
            return redirect('../viewreservations')
    else:
        form = ReservationForm()
    return render(request, 'hoteladmin/reserve.html', {'form': form})

@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('viewreservation')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'hoteladmin/reserve.html', {'form': form, 'reservation': reservation})

@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('viewreservation')

@login_required
def update(request):
    context={
        "Reservations": Reservation.objects.all()
    }
    return render(request, 'hoteladmin/update.html', context)

@login_required
def cancel(request):
    context={
        "Reservations": Reservation.objects.all()
    }
    return render(request, 'hoteladmin/cancel.html', context)

@login_required
def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'hoteladmin/chat.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.all()
    return render(request, 'hoteladmin/inbox.html', {'messages': messages})
