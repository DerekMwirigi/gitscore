from rest_framework import serializers


class GitHubRepositorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    score = serializers.IntegerField(min_value=250)
    popularity = serializers.BooleanField()


class CheckGitHubRespositoryRequestSerializer(serializers.Serializer):
    organisation = serializers.CharField(max_length=32)
    reposiroty = serializers.CharField(max_length=32)


class CheckGitHubRespositoryResponseSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    errors = serializers.ListField(child=serializers.CharField())
    message = serializers.CharField(max_length=32)
    data = GitHubRepositorySerializer(many=False)
