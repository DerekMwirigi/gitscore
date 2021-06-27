from django.test import TestCase
from apps.user.models import User

from rest_framework.authtoken.models import Token
from apps.user.tasks import create_user_token

class TestAppTasks(TestCase):
    def test_create_user_token(self):
        test_user_1 = User.objects.create(username='Uname1', password='12345')
        token, created = Token.objects.get_or_create(user=test_user_1)
        self.assertEqual(create_user_token(test_user_1), token)