from random import randint

text_game = 'What is the result of the expression?'

def question_game():
    a = f'{randint(1, 100)} - {randint(1, 100)}'
    b = f'{randint(1, 100)} + {randint(1, 100)}'
    c = f'{randint(1, 10)} * {randint(1, 10)}'
    options = (a, b, c)
    x = options[randint(0,2)]
    y = eval(x)
    return [x, y] 
