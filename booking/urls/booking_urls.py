# Booking/booking/urls/booking_urls.py
from django.urls import path
from booking.views.booking_views import BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
    path('<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-retrieve-update-destroy'),
]
