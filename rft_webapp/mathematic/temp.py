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
            if second_numb > first_numb:
                first_numb, second_numb = second_numb, first_numb
                x = first_numb - second_numb
            else:
                x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            first_numb = random.randrange(1, 21)
            second_numb = random.randrange(1, 21)
            x = first_numb * second_numb
        else:
            first_numb = random.randrange(2, 21)
            while True:
                second_numb = random.randrange(1, 21)
                if first_numb == 1:
                    break
                print("second number = {}".format(second_numb))
                if first_numb != second_numb and first_numb % second_numb == 0:
                    break
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)


    def intermediate(self):
        ops = ['+', '-', '*']
        op1 = random.choice(ops)
        op2 = random.choice(ops)
        op3 = random.choice(ops)
        op4 = random.choice(ops)

        n1 = random.randrange(1,11)
        n2 = random.randrange(1,11)
        n3 = random.randrange(1,11)
        n4 = random.randrange(1,11)
        n5 = random.randrange(1,11)


        question = "({n1} {op1} {n2}) {op2} ({n3} {op3} {n4})".format(n1=n1, n2=n2, n3=n3, n4=n4, op1=op1, op2=op2, op3=op3)
        correct_answer = eval(question)
        question += " = "

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
            if second_numb > first_numb:
                first_numb, second_numb = second_numb, first_numb
                x = first_numb - second_numb
            else:
                x = first_numb - second_numb
        elif operator == enums.Operator.MULTIPLICATION:
            first_numb = random.randrange(1, 41)
            second_numb = random.randrange(1, 41)
            x = first_numb * second_numb
        else:
            first_numb = random.randrange(2, 41)
            while True:
                second_numb = random.randrange(1, 41)
                if first_numb == 1:
                    break
                print("second number = {}".format(second_numb))
                if first_numb != second_numb and first_numb % second_numb == 0:
                    break;
            x = first_numb / second_numb

        question = "{} {} {}=".format(first_numb, operator.value, second_numb)
        correct_answer = x

        return (question, correct_answer)
