import prompt
import random


def is_even(num):
    return num % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        question = random.randint(0, 1000)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()

        correct_answer = 'yes' if is_even(question) else 'no'

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

            return 0

    print(f"Congratulations, {name}!")

    return 1


if __name__ == '__main__':
    main()
