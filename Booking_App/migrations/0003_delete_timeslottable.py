# Generated by Django 3.2.8 on 2021-11-17 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0002_bookingtable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeSlotTable',
        ),
    ]