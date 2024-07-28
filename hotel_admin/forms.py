from django import forms
from django.forms import ModelForm 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hotel_app.forms import ReservationForm, CreateUserForm, RoomForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'content']