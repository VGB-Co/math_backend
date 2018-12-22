from django.db import models

from rft_webapp.mathematic.enums import Type, Operator

list = [Operator.PLUS, Operator.MINUS, Operator.DIVISION, Operator.MULTIPLICATION]


class Task(models.Model):
    
    correct_answer = models.IntegerField()
    question = models.TextField()
    difficulty = models.IntegerField()

    class Meta:
        managed = True