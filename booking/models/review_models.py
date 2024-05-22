from django.db import models
from booking.models.user_models import User
from booking.models.hotel_models import Hotel

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for hotel {self.hotel.name}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
