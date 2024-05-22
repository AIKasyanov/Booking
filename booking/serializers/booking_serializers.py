# Booking/booking/serializers/booking_serializers.py
from rest_framework import serializers
from booking.models.booking_models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
