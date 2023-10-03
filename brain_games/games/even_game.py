import random
from brain_games.games.games_engine import launch_game
from brain_games.games.games_constants import MAX_NUMBER


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(0, MAX_NUMBER)
    return (number, 'yes' if is_even(number) else 'no')


def run_game():
    launch_game(generate_round, game_rules)
