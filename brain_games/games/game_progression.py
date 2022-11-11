from random import randint

text_game = 'What number is missing in the progression?'

def list1():
    l = []
    i = 0
    n = randint(1, 100)
    k = randint(1, 10)
    while i < 10:
        l.append(1 + n)
        i += 1
        n += k
    m = randint(0, 9)
    j = l[m]
    l[m] = '..'
    return [j, l]

def question_game():
    x = 1
    y = 1
    [x, y] = list1()
    return [y, x]
