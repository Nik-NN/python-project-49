from random import randint


RULE = 'What number is missing in the progression?'


def progression():
    num = randint(1, 100)
    progression_list = []
    i = 0
    stride_length = randint(1, 10)
    while i < 10:
        progression_list.append(1 + num)
        i += 1
        num += stride_length
    return progression_list

def question_game():
    progression_list = progression()
    hidden_element_num = randint(0, 9)
    answer = progression_list[hidden_element_num]
    progression_list[hidden_element_num] = '..'
    question = str(progression_list).replace("'", "")
    return question.replace(",", "")[1:-1], answer
