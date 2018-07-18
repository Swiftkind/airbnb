from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    """ User model """
    email = models.EmailField(max_length=225, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(null=True)
    cover_image = models.FileField(upload_to='images/',default=None,null=True)

    is_host = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name","birth_date")


    def __str__(self):
        return f"{self.email}"

    def get_short_name(self):
        return f"{self.first_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    @property
    def get_display_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name
        return f"{self.email}"


class Confirmation(models.Model):
    """ change password confirmation model
    """
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    url = models.CharField(max_length=500, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        self.url = reverse('users:changepass', args={str(self.id)})

        return super(Confirmation, self).save(*args, **kwargs)

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)
    expiration = models.CharField(max_length=20)
    cvv = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)