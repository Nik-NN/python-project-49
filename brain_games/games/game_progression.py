from random import randint

text_game = 'What number is missing in the progression?'

def progression():
    progression_list = []
    i = 0
    n = randint(1, 100)
    stride_length = randint(1, 10)
    while i < 10:
        progression_list.append(1 + n)
        i += 1
        n += stride_length
    hidden_element = randint(0, 9)
    j = progression_list[hidden_element]
    progression_list[hidden_element] = '..'
    return [progression_list, j]

def question_game():
    [question, answer] = progression()
    return [question, answer]
