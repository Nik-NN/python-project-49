from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(num):
    if num % 2 == 0:
        return True
    else:
        return False


def question_game():
    question = randint(1, 100)
    answer = ''
    if check_parity(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
