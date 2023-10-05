import random
import operator


DESCRIPTION = 'What is the result of the expression?'


get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}.get


def generate_round():
    MAX_NUMBER = 100
    OPERATIONS = ['+', '-', '*']

    number_a = random.randint(0, MAX_NUMBER)
    number_b = random.randint(0, MAX_NUMBER)
    random_operation = OPERATIONS[random.randint(0, len(OPERATIONS) - 1)]

    question = f'{number_a} {random_operation} {number_b}'
    operation = get_operator(random_operation)
    answer = str(operation(number_a, number_b))
    return (question, answer)
