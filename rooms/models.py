from django.db import models

from accounts.models import User

class PropertyType(models.Model):
    """ Property type """
    name = models.CharField(max_length=255)

class Amenity(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Property(models.Model):
    """ Property / Rooms """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    amenities = models.ManyToManyField(Amenity)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    number_of_guests = models.IntegerField(default=0)
    number_of_beds = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    is_deleted = models.BooleanField(default=False)





