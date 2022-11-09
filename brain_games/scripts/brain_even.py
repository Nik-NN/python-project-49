from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 4:
        if i == 3:
            print(f'Congratulations, {name}!')
            break
        x = randint(1,100)
        print(f'Question:{x}')
        print('Your answer:', end='')
        answer = input()
        if x % 2 == 0 and answer == 'yes':
            print('Correct!')
            i += 1
        elif x % 2 == 1 and answer == 'no':
            print('Correct!')
            i += 1
        elif x % 2 == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            break
        elif x % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
            print(f"Let's try again, {name}!")
            break
    
    

if __name__ == '__main__':
    main()
