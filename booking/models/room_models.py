from django.db import models
from booking.models.hotel_models import Hotel

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='room_photos/')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room_type} at {self.hotel.name}"

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
