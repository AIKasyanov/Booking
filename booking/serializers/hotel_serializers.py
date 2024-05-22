# Booking/booking/serializers/Hotel_serializers.py
from rest_framework import serializers
from booking.models.hotel_models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
