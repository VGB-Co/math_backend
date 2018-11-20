from rest_framework import serializers
from rft_webapp.math import task


class TaskSerializer(serializers.JSONField):
    class Meta:
        model = task
        fields = ('question', 'correct_answer')