from random import randint

text_game = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    i = num1 + num2
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
            break
        else:
            i -= 1

def question_game():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    result = gcd(num1, num2)
    x = f'{num1} {num2}'
    y = result
    return [x, y]

