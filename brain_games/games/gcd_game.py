import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def generate_round():
    MAX_NUMBER = 100

    number_a = random.randint(0, MAX_NUMBER)
    number_b = random.randint(0, MAX_NUMBER)

    question = f'{number_a} {number_b}'

    answer = gcd(number_a, number_b)
    return (question, str(answer))
