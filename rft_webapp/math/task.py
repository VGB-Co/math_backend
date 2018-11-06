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
    first_numb = randrange(0, 101)
    operator = random.choice(list)
    second_numb = randrange(0, 101, first_numb)

    if operator == Operator.PLUS:
        x = first_numb + second_numb
    elif operator == Operator.MINUS:
        x = first_numb - second_numb
    elif operator == Operator.MULTIPLICATION:
        x = first_numb * second_numb
    else:
        x = first_numb / second_numb

    return (first_numb, operator, second_numb, x)


def intermediate():
    first_numb = randrange(0, 1001)
    operator = random.choice(list)
    second_numb = randrange(0, 1001, first_numb)

    if operator == Operator.PLUS:
        x = first_numb + second_numb
    elif operator == Operator.MINUS:
        x = first_numb - second_numb
    elif operator == Operator.MULTIPLICATION:
        x = first_numb * second_numb
    else:
        x = first_numb / second_numb

    return (first_numb, operator, second_numb, x )


def advanced():
    first_numb = randrange(0, 10001)
    operator = random.choice(list)
    second_numb = randrange(0, 10001, first_numb)

    if operator == Operator.PLUS:
        x = first_numb + second_numb
    elif operator == Operator.MINUS:
        x = first_numb - second_numb
    elif operator == Operator.MULTIPLICATION:
        x = first_numb * second_numb
    else:
        x = first_numb / second_numb

    return (first_numb, operator, second_numb, x)
