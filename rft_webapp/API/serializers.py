from rest_framework import serializers
from rft_webapp.mathematic.models import Task


class TaskSerializer(serializers.Serializer):

    correct_answer = serializers.IntegerField()
    question = serializers.CharField()

class TopListSerializer(serializers.Serializer):

    user = serializers.IntegerField()
    type = serializers.IntegerField()
    score = serializers.IntegerField()
    time = serializers.FloatField()