from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    bookings = models.ManyToManyField('Booking', related_name='users', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='booking_users',  # Уникальное имя для обратной связи
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='booking_users',  # Уникальное имя для обратной связи
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
