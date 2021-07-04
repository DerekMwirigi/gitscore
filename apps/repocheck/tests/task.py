from django.test import TestCase

from apps.repocheck.tasks import evaluate_repository


class TestAppTasks(TestCase):
    def test_evaluate_repository(self):
        repository = {'name': 'test', 'stargazers_count': 2, 'forks_count': 2}
        self.assertEqual(evaluate_repository(repository), {'name': 'test', 'score': 6, 'popularity': False})
