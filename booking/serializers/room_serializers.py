# Booking/booking/serializers/Room_serializers.py
from rest_framework import serializers
from booking.models.room_models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
