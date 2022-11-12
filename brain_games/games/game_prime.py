from random import randint

text_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def prime(num):
    i = 2
    divisor_counter = 0
    while i <= num:
        if num % i == 0:
            divisor_counter += 1
            i += 1
        else:
            i += 1
    if divisor_counter == 1:
        return 'yes'
    else:
        return 'no'


def question_game():
    num1 = randint(2, 500)
    question = num1
    answer = prime(num1)
    return [question, answer]
