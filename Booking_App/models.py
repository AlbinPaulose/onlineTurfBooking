from django.db import models
from django.contrib.auth.models import User



class BookingTable(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    hours_need = models.IntegerField(default=1)
    booking_date = models.DateField()
    time_slot = models.CharField(max_length=30)
    amount = models.IntegerField()
    note = models.TextField(blank=True)
    book_status = models.CharField(max_length=20)
