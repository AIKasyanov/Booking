# Generated by Django 5.0.3 on 2024-05-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('booking', '0003_alter_booking_deleted_at_alter_review_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookings',
            field=models.ManyToManyField(blank=True, related_name='users', to='booking.booking'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='users', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='users', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]