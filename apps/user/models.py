from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
import jwt


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
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.encode().decode('utf-8')
