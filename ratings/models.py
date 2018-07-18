from django.db import models

from rooms.models import Property

class Rating(models.Model):
    property_for_rent = models.ForeignKey(Property,on_delete=models.CASCADE)
    feedback = models.TextField()
    rate = models.IntegerField(default=1)