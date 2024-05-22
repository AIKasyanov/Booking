# Generated by Django 5.0.3 on 2024-05-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='room_id',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='hotel_id',
            new_name='hotel',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='hotel_id',
            new_name='hotel',
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('room', 'check_in_date', 'check_out_date')},
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
