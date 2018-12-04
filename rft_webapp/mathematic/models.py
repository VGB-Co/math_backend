from django.db import models

from rft_webapp.mathematic.enums import Type, Operator

list = [Operator.PLUS, Operator.MINUS, Operator.DIVISION, Operator.MULTIPLICATION]


class Task(models.Model):
    
    correct_answer = models.IntegerField()
    question = models.TextField()

    class Meta:
        managed = True