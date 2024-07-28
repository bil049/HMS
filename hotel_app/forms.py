from django import forms
from django.forms import ModelForm 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'name', 'room_number', 'room_type', 'check_in', 'check_out']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'is_available']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'content']

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['service', 'date', 'time']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        
              