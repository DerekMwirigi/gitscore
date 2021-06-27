from rest_framework import serializers

class GitHubRepository_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    score = serializers.IntegerField(min_value=250)
    popularity = serializers.BooleanField()


class CheckGitHubOrganisationRepositoryReponse_Serializer(serializers.Serializer):
    status = serializers.BooleanField()
    errors = serializers.ListField(child=serializers.CharField())
    message = serializers.CharField(max_length=32)
    data = GitHubRepository_Serializer(many=True)

class CheckGitHubRepositoryReponse_Serializer(serializers.Serializer):
    status = serializers.BooleanField()
    errors = serializers.ListField(child=serializers.CharField())
    message = serializers.CharField(max_length=32)
    data = GitHubRepository_Serializer(many=False)
