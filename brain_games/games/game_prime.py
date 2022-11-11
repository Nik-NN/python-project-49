from random import randint

text_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def func1(num):
    i = 2
    k = 0
    while i <= num:
        if num % i == 0:
            k += 1
            i += 1
        else:
            i += 1
    if k == 1:
        return 'yes'
    else:
        return 'no'


def question_game():
    num1 = randint(2, 500)
    x = func1(num1)
    y = num1
    return [y, x]
