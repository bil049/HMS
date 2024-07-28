from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name="index"),
path('index/', views.index),
path('home/', views.home),
path('register/', views.register),
path('login/', views.loginPage),
path('logout/', views.logoutUser, name="logout"),
path('makereservation/', views.makereservation),
path('reserve/', views.reserve, name="reserve1"),
path('reservation1/', views.reservation, name="reservation1"),
path('update/<int:pk>/', views.update_reservation, name="update1"),
path('cancel/<int:pk>/', views.cancel_reservation, name="cancel1"),
path('update/', views.update, name="upUI1"),
path('cancel/', views.cancel, name="caUI1"),
path('available/', views.available, name="available"),
path('chat/', views.compose_message, name="chat"),
path('inbox/', views.inbox, name="inbox1"),
path('extraservices/', views.extra, name='extra'),
path('bookservice/', views.bookservice, name='bookservice'),
path('bookedservices', views.bookedservice, name='booked')
]