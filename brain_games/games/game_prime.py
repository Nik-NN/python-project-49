from random import randint


text_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    i = 2
    divisor_counter = 0
    while i <= num:
        if num % i == 0:
            divisor_counter += 1
        elif divisor_counter > 1:
            return 'no'
            break
        elif i == num - 1 and divisor_counter == 0:
            return 'yes'
        i += 1


def question_game():
    num1 = randint(2, 500)
    question = num1
    answer = prime(num1)
    return [question, answer]
