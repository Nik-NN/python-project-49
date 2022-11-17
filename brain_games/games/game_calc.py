import random

RULE = 'What is the result of the expression?'


def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def question_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator_list = ['-', '+', '*']
    operator = random.choice(operator_list)
    question = f'{num1} {operator} {num2}'
    answer = calc(num1, num2, operator)
    return question, answer
