import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    MAX_NUMBER = 100

    number = random.randint(0, MAX_NUMBER)
    return (number, 'yes' if is_even(number) else 'no')
