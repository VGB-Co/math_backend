from enum import Enum


class Type(Enum):
    EASY = 0
    INTERMEDIATE = 1
    ADVANCED = 2


class Operator(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
