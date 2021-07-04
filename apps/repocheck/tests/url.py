from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from apps.user.models import User


class TestGithubRepositoryScoreURL(APITestCase):
    def test_post(self):
        url = reverse('github_repo_score')
        data = {'organisation': 'google', 'repository': 'file.dart'}
        test_user = User.objects.create(username='test', password='password')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_user.token)
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [200, 401])
        self.assertRaises(KeyError, lambda: response.json()['name'])
