import random
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(round(math.sqrt(number))) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    MAX_NUMBER = 100

    number = random.randint(0, MAX_NUMBER)
    return (number, 'yes' if is_prime(number) else 'no')
