from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def question_game():
    question = randint(1, 100)
    answer = ''
    if even(question) == True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
