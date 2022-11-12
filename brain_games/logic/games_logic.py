import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.text_game)
    i = 0
    while i < 4:
        if i == 3:
            print(f'Congratulations, {name}!')
            break
        [question_game, correct_answer] = game.question_game()
        print(f'Question:{question_game}')
        print('Your answer:', end='')
        answer = input()
        if answer == f'{correct_answer}':
            print('Correct!')
            i += 1
        elif answer != f'{correct_answer}':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
