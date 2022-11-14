from random import randint


text_game = 'What number is missing in the progression?'


def progression(num):
    progression_list = []
    i = 0
    stride_length = randint(1, 10)
    while i < 10:
        progression_list.append(1 + num)
        i += 1
        num += stride_length
    hidden_element_num = randint(0, 9)
    hidden_element = progression_list[hidden_element_num]
    progression_list[hidden_element_num] = '..'
    progression_list_str = str(progression_list)
    return [progression_list_str.replace("'", ""), hidden_element]


def question_game():
    num = randint(1, 100)
    [question, answer] = progression(num)

    return [question[1:-1], answer]
 