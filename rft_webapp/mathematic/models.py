from django.db import models

from random import randrange, random

from rft_webapp.mathematic.enums import Type, Operator

list = [Operator.PLUS, Operator.MINUS, Operator.DIVISION, Operator.MULTIPLICATION]


class Task(models.Model):
    
    correct_answer = models.IntegerField()
    question = models.TextField()

    class Meta:
        managed = True

    # def __init__(self, level):
    #     self.level = level
    #     if level == Type.EASY:
    #         self.question, self.correct_answer = self.easy()
    #     elif level == Type.INTERMEDIATE:
    #         self.question, self.correct_answer = self.intermediate()
    #     else:
    #         self.question, self.correct_answer = self.advanced()


    # def easy(self):
    #     first_numb = randrange(0, 101)
    #     operator = random.choice(list)
    #     second_numb = randrange(0, 101, first_numb)

    #     if operator == Operator.PLUS:
    #         x = first_numb + second_numb
    #     elif operator == Operator.MINUS:
    #         x = first_numb - second_numb
    #     elif operator == Operator.MULTIPLICATION:
    #         x = first_numb * second_numb
    #     else:
    #         x = first_numb / second_numb

    #     question = first_numb + operator + second_numb
    #     correct_answer = x

    #     return (question, correct_answer)


    # def intermediate(self):
    #     first_numb = randrange(0, 1001)
    #     operator = random.choice(list)
    #     second_numb = randrange(0, 1001, first_numb)

    #     if operator == Operator.PLUS:
    #         x = first_numb + second_numb
    #     elif operator == Operator.MINUS:
    #         x = first_numb - second_numb
    #     elif operator == Operator.MULTIPLICATION:
    #         x = first_numb * second_numb
    #     else:
    #         x = first_numb / second_numb

    #     question = first_numb + operator + second_numb
    #     correct_answer = x

    #     return (question, correct_answer)


    # def advanced(self):
    #     first_numb = randrange(0, 10001)
    #     operator = random.choice(list)
    #     second_numb = randrange(0, 10001, first_numb)

    #     if operator == Operator.PLUS:
    #         x = first_numb + second_numb
    #     elif operator == Operator.MINUS:
    #         x = first_numb - second_numb
    #         x = first_numb - second_numb
    #     elif operator == Operator.MULTIPLICATION:
    #         x = first_numb * second_numb
    #     else:
    #         x = first_numb / second_numb

    #     question = first_numb + operator + second_numb
    #     correct_answer = x

    #     return (question, correct_answer)
