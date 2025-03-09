import prompt
from random import randint

def is_even(number):
    return number % 2 == 0

def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    amount = 0
    while amount < 3:
        question = randint(1, 1000)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(question) else 'no'

        if correct_answer == answer:
            print('Correct!')
            amount += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.)")
            break

    if amount == 3:
        print(f'Congratulations, {name}!')