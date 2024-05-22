from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from booking.models.booking_models import Booking
from booking.models.hotel_models import Hotel
from booking.models.review_models import Review
from booking.models.room_models import Room
from booking.models.user_models import User


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description', 'photos', 'rating',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('name', 'location')
    search_fields = ('name', 'location')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'photos', 'price_per_night', 'available',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('room_type', 'price_per_night', 'available')
    search_fields = ('room_type', 'price_per_night')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in_date', 'check_out_date',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('room', 'check_in_date', 'check_out_date')
    search_fields = ('room', 'check_in_date', 'check_out_date')


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'comment', 'rating',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('hotel', 'rating')
    search_fields = ('rating', 'comment')
