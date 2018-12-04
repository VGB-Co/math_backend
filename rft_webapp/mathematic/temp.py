from rft_webapp.mathematic import enums
import random

list = [enums.Operator.PLUS, enums.Operator.MINUS, enums.Operator.DIVISION, enums.Operator.MULTIPLICATION]

class Generating():

    def __init__(self, level):
        self.level = level
        if level == enums.Type.EASY:
            self.question, self.correct_answer = self.easy()
        elif level == enums.Type.INTERMEDIATE:
            self.question, self.correct_answer = self.intermediate()
        else:
            self.question, self.correct_answer = self.advanced()


    def easy(self):
        first_numb = random.randrange(1, 101)
        operator = random.choice(list)
        second_numb = random.randrange(1, 101, first_numb - 1)

        if operator == enums.Operator.PLUS:
            x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            x = first_numb * second_numb
        else:
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)


    def intermediate(self):
        first_numb = random.randrange(1, 1001)
        operator = random.choice(list)
        second_numb = random.randrange(1, 1001, first_numb - 1)

        if operator == enums.Operator.PLUS:
            x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            x = first_numb * second_numb
        else:
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)

    def advanced(self):
        first_numb = random.randrange(1, 10001)
        operator = random.choice(list)
        second_numb = random.randrange(1, 10001, first_numb - 1)

        if operator == enums.Operator.PLUS:
            x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            x = first_numb * second_numb
        else:
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)