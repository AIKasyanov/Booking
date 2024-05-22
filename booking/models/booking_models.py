from django.db import models
from django.core.exceptions import ValidationError
from booking.models.user_models import User
from booking.models.room_models import Room


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.room} from {self.check_in_date} to {self.check_out_date}"

    def clean(self):
        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_in_date__lt=self.check_out_date,
            check_out_date__gt=self.check_in_date,
            deleted=False
        ).exclude(pk=self.pk)

        if overlapping_bookings.exists():
            raise ValidationError(f'The room {self.room} is already booked for the selected dates.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        unique_together = ('room', 'check_in_date', 'check_out_date')
