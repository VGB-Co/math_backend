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
        first_numb = random.randrange(1, 51)
        operator = random.choice(list)

        if operator == enums.Operator.PLUS:
                second_numb = random.randrange(1, 51)
                if first_numb == second_numb:
                    second_numb = random.randrange(1, 51)
                x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            second_numb = random.randrange(1, 51)
            if first_numb == second_numb:
                second_numb = random.randrange(1, 51)
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            first_numb = random.randrange(1, 21)
            second_numb = random.randrange(1, 21)
            x = first_numb * second_numb
        else:
            first_numb = random.randrange(1, 21)
            while True:
                second_numb = random.randrange(1, 21)
                if first_numb % second_numb == 0 and first_numb != second_numb:
                    break;
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)


    def intermediate(self):
        first_numb = random.randrange(1, 101)
        operator = random.choice(list)

        if operator == enums.Operator.PLUS:
            second_numb = random.randrange(1, 101)
            if first_numb == second_numb:
                second_numb = random.randrange(1, 101)
            x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            second_numb = random.randrange(1, 101)
            if first_numb == second_numb:
                second_numb = random.randrange(1, 101)
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            first_numb = random.randrange(1, 31)
            second_numb = random.randrange(1, 31)
            x = first_numb * second_numb
        else:
            first_numb = random.randrange(1, 31)
            while True:
                second_numb = random.randrange(1, 31)
                if first_numb % second_numb == 0 and first_numb != second_numb:
                    break;
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)

    def advanced(self):
        first_numb = random.randrange(1, 151)
        operator = random.choice(list)

        if operator == enums.Operator.PLUS:
            second_numb = random.randrange(1, 151)
            if first_numb == second_numb:
                second_numb = random.randrange(1, 151)
            x = first_numb + second_numb
        elif operator == enums.Operator.MINUS:
            second_numb = random.randrange(1, 151)
            if first_numb == second_numb:
                second_numb = random.randrange(1, 151)
            x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            first_numb = random.randrange(1, 41)
            second_numb = random.randrange(1, 41)
            x = first_numb * second_numb
        else:
            first_numb = random.randrange(1, 41)
            while True:
                second_numb = random.randrange(1, 41)
                if first_numb % second_numb == 0 and first_numb != second_numb:
                    break;
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)