# Generated by Django 3.2.8 on 2021-11-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0003_delete_timeslottable'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtable',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
