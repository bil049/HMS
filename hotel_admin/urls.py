from django.urls import path
from . import views


urlpatterns = [
    path('room/', views.room, name='room'),
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('registeruser/', views.register),
    path('users/', views.users, name='users'),
    path('users/<int:pk>/', views.updateuser, name='updateuser'),
    path('users/<int:pk>/', views.canceluser, name='canceluser'),
    path('login', views.admin_dashboard, name='admin_dashboard'),
    path('viewrooms/', views.manage_room, name='rooms'),
    path('rooms/create/', views.create_room, name='create_room'),
    path('rooms/<int:pk>/edit/', views.edit_room, name='edit_room'),
    path('rooms/<int:pk>/delete/', views.cancel_room, name='delete_room'),
    path('viewreservations/', views.viewreservation, name="viewreservation"),
    path('reservation/', views.reservation, name='reservation'),
    path('reserve/', views.reserve, name="reserve"),
    path('update/<int:pk>/', views.update_reservation, name="update"),
    path('cancel/<int:pk>/', views.cancel_reservation, name="cancel"),
    path('update/', views.update, name="upUI"),
    path('cancel/', views.cancel, name="caUI"),
    path('updateroom/', views.updateroom, name="uprooomUI"),
    path('cancelroom/', views.cancelroom, name="caroomUI"),
    path('chat/', views.compose_message, name="chat"),
    path('inbox/', views.inbox, name="inbox")

]
