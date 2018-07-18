from django.db import models

from rooms.models import Property
from accounts.models import User

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    property_rented  = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(auto_now=True)
    check_out_date = models.DateTimeField(auto_now=True)
    number_of_guests = models.IntegerField(default=0)
    number_of_nights = models.FloatField(default=0)
    price_upon_booking = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    service_fee = models.FloatField(default=0)
    total_amount_paid = models.FloatField(default=0)
    is_canceled = models.BooleanField(default=False) 
