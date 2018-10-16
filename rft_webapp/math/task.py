#!/usr/bin/env python
from random import randrange, random

from rft_webapp.math.enums import Type, Operator

list = [Operator.PLUS, Operator.MINUS, Operator.DIVISION, Operator.MULTIPLICATION]

class Task:
    level = None

    def tasks(level):

        if level == Type.EASY:
            easy()
        elif level == Type.INTERMEDIATE:
            intermediate()
        else:
            advanced()


def easy():

    firstnumb = randrange(0, 101)
    operator = random.choice(list)
    secondnumb = randrange(0, 101, firstnumb)

    if operator == Operator.PLUS:
        x = firstnumb + secondnumb
    elif operator == Operator.MINUS:
        x = firstnumb - secondnumb
    elif operator == Operator.MULTIPLICATION:
        x = firstnumb * secondnumb
    else:
        x = firstnumb / secondnumb

    return (firstnumb, operator, secondnumb, x)

def intermediate():
    firstnumb = randrange(0, 1001)
    operator = random.choice(list)
    secondnumb = randrange(0, 1001, firstnumb)

    if operator == Operator.PLUS:
        x = firstnumb + secondnumb
    elif operator == Operator.MINUS:
        x = firstnumb - secondnumb
    elif operator == Operator.MULTIPLICATION:
        x = firstnumb * secondnumb
    else:
        x = firstnumb / secondnumb

    return (firstnumb, operator, secondnumb, x)


def advanced():
    firstnumb = randrange(0, 10001)
    operator = random.choice(list)
    secondnumb = randrange(0, 10001, firstnumb)

    if operator == Operator.PLUS:
        x = firstnumb + secondnumb
    elif operator == Operator.MINUS:
        x = firstnumb - secondnumb
    elif operator == Operator.MULTIPLICATION:
        x = firstnumb * secondnumb
    else:
        x = firstnumb / secondnumb

    return (firstnumb, operator, secondnumb, x)
