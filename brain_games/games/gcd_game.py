import random
from brain_games.games.games_engine import launch_game
from brain_games.games.games_constants import MAX_NUMBER


game_rules = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def generate_round():
    random_number_a = random.randint(0, MAX_NUMBER)
    random_number_b = random.randint(0, MAX_NUMBER)

    question = f'{random_number_a} {random_number_b}'

    answer = gcd(random_number_a, random_number_b)
    return (question, str(answer))


def run_game():
    launch_game(generate_round, game_rules)
