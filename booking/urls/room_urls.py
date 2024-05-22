# Booking/booking/urls/room_urls.py
from django.urls import path
from booking.views.room_views import RoomListCreateView, RoomRetrieveUpdateDestroyView, AvailableRoomsListView

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='room-list'),
    path('<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(), name='room-retrieve-update-destroy'),
]
