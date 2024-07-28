from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    ROOM_TYPE=(
        ('Standard', 'Standard'),
        ('Executive', 'Executive'), 
        ('Adjoining', 'Adjoining'),
        ('Presidential Suite', 'Presidential Suite')
    )
    STATUS= (
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled')
    )
    name = models.CharField(max_length=100)
    room_number=models.IntegerField(null=True)
    room_type=models.CharField(max_length=120, null= True, choices=ROOM_TYPE)
    check_in = models.DateField()
    check_out = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status =models.CharField(max_length=120, default='Booked', choices=STATUS)
    
    def __str__(self):
        return self.room_type
    
class Room(models.Model):
    ROOM_TYPE=(
        ('Standard', 'Standard'),
        ('Executive', 'Executive'), 
        ('Adjoining', 'Adjoining'),
        ('Presidential Suite', 'Presidential Suite')
    )
    room_number=models.IntegerField(null=True)
    room_type=models.CharField(max_length=120, null=True, choices=ROOM_TYPE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Service(models.Model):
    SERVICE=(
        ('Pick-Up', 'Pick-Up'),
        ('Drop-Off', 'Drop-Off')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service=models.CharField(max_length=120, null=True, choices=SERVICE)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    
