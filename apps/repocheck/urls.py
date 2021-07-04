from django.urls import path
from .views import check_github_repository_score


url_prefix = 'github/'

api_urls = [
    path(url_prefix + 'score/repository/<organisation>/<repository>', check_github_repository_score, name="github_repo_score"),
]
