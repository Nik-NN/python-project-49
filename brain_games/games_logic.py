import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    i = 0
    rounds = 3
    while i < rounds:
        [question_game, correct_answer] = game.question_game()
        print(f'Question: {question_game}')
        print('Your answer:', end='')
        answer = input()
        if answer == f'{correct_answer}':
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
