from django.urls import path
from .views import *

url_prefix = 'github/'

api_urls = [
    path(url_prefix + 'organisation/repositories/<organisation>', check_github_organisation_repositories_score, name="github_organisation_repositories_score"),
    path(url_prefix + 'score/repository/<organisation>/<repository>', check_github_repository_score, name="github_repo_score"),
]