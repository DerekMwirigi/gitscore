from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

import requests

from apps.repocheck.serializers import CheckGitHubRespositoryRequestSerializer, \
    CheckGitHubRespositoryResponseSerializer

from apps.repocheck.tasks import evaluate_repository


class GithubRepositoryScoreAPIView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=CheckGitHubRespositoryRequestSerializer,
        responses={
            200: CheckGitHubRespositoryResponseSerializer
        },
        security=[],
        operation_id='Github repository score',
        operation_description='Github repository score',
        tags=['Github repository score'],
    )
    def post(self, request, format=None):
        reponse = {'status': False, 'message': 'Failed', 'errors': [], 'data': []}
        status_code = status.HTTP_200_OK
        url = 'https://api.github.com/repos/{}/{}'.format(request.data['organisation'], request.data['repository'])
        http_reponse = requests.get(url=url)
        status_code = http_reponse.status_code
        if status_code == 200:
            repo_json_response = http_reponse.json()
            reponse = {'status': True, 'message': 'Success', 'errors': [], 'data': evaluate_repository(repo_json_response)}
        return Response(reponse, status=status_code)
