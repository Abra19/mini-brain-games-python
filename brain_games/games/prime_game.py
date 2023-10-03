import random
import math
from brain_games.games.games_engine import launch_game
from brain_games.games.games_constants import MAX_NUMBER


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(round(math.sqrt(number))) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(0, MAX_NUMBER)
    return (number, 'yes' if is_prime(number) else 'no')


def run_game():
    launch_game(generate_round, game_rules)
