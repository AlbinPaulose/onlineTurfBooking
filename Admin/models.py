from django.db import models

book_status = (
    ("Pending", "pending"),
    ("Paid", "paid"),
    ("Cancelled", "cancelled"),
    ("Refunded", "refunded")
)


# Create your models here.
class TimeSlotTable(models.Model):
    time_slot = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

# Create your models here.
class TurfDetails(models.Model):
    turf_name=models.CharField(max_length=50)
    turf_place=models.CharField(max_length=50)
    turf_morningPrice=models.IntegerField()
    turf_eveningPrice=models.IntegerField()
    turf_number=models.CharField(max_length=10)
    turf_address=models.CharField(max_length=70)

    def __str__(self):
        return str(self.turf_name)
