from django.urls import path
from apps.repocheck.views import GithubRepositoryScoreAPIView


url_prefix = 'github/'

api_urls = [
    path(url_prefix + 'score/repository/', GithubRepositoryScoreAPIView.as_view(), name="github_repo_score"),
]
