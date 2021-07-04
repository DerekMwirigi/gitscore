from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

import requests

from apps.repocheck.serializers import CheckGitHubRepositoryReponse_Serializer

from apps.repocheck.tasks import evaluate_repository


organisation = openapi.Parameter('organisation', openapi.IN_QUERY, description="organisation param", type=openapi.TYPE_STRING)
repository = openapi.Parameter('repository', openapi.IN_QUERY, description="repository param", type=openapi.TYPE_STRING)
reposcore_response = openapi.Response('response description', CheckGitHubRepositoryReponse_Serializer)


@swagger_auto_schema(method='get', manual_parameters=[organisation, repository], responses={200: reposcore_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def check_github_repository_score(request, organisation, repository):
    reponse = {'status': False, 'message': 'Failed', 'errors': [], 'data': []}
    status_code = status.HTTP_200_OK
    url = 'https://api.github.com/repos/{}/{}'.format(organisation, repository)
    http_reponse = requests.get(url=url)
    status_code = http_reponse.status_code
    if status_code == 200:
        repo_json_response = http_reponse.json()
        reponse = {'status': True, 'message': 'Success', 'errors': [], 'data': evaluate_repository(repo_json_response)}
        print(repo_json_response)
    return Response(reponse, status=status_code)
