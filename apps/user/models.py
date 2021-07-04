from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    A base user for auth and extending
    """
    phone_number = models.CharField(max_length=12, default='')
    email = models.CharField(max_length=50, unique=True)

    @property
    def full_names(self):
        return "{} {}".format(self.first_name.capitalize(), self.last_name.capitalize())

    @property
    def get_phone(self):
        return self.phone_number

    @property
    def get_email(self):
        return self.email
