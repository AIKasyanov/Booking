# Booking/booking/serializers/Review_serializers.py
from rest_framework import serializers
from booking.models.review_models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
