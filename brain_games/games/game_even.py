from random import randint

text_game = 'Answer "yes" if the number is even, otherwise answer "no".'

def even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_game():
    question = randint(1, 100)
    answer = even(question)
    return [question, answer]

