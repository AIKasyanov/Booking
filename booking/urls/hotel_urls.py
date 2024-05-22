# Booking/booking/urls/hotel_urls.py
from django.urls import path
from booking.views.hotel_views import HotelListCreateView, HotelRetrieveUpdateDestroyView
from booking.views.room_views import AvailableRoomsListView

urlpatterns = [
    path('', HotelListCreateView.as_view(), name='hotel-list'),
    path('<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel-retrieve-update-destroy'),
    path('rooms/', AvailableRoomsListView.as_view(), name='available-rooms-list'),
]
