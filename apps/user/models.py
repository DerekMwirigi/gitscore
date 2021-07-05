from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


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

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)
