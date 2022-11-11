from random import randint

text_game = 'Answer "yes" if the number is even, otherwise answer "no".'

def even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_game():
    num1 = randint(1, 100)
    x = num1
    y = even(num1)
    return [x, y]

