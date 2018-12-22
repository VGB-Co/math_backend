from enum import IntEnum, Enum


class Type(IntEnum):
    EASY = 0
    INTERMEDIATE = 1
    ADVANCED = 2


class Operator(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
