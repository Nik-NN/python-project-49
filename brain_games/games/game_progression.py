from random import randint


RULE = 'What number is missing in the progression?'


def generate_progression(initial_value, stride_length, progression_length):
    progression_list = []
    i = 0
    while i < progression_length:
        progression_list.append(1 + initial_value)
        i += 1
        initial_value += stride_length
    return progression_list


def question_game():
    initial_value = randint(1, 100)
    stride_length = randint(1, 10)
    progression_list = generate_progression(initial_value, stride_length, 10)
    hidden_element_num = randint(0, 9)
    answer = progression_list[hidden_element_num]
    progression_list[hidden_element_num] = '..'
    question = progression_list
    question = [str(i) for i in question]
    question = ' '.join(question)
    return question, answer
