import prompt
from brain_games.games.games_constants import ROUNDS_NUMBER


def launch_game(generate_round, game_rules):
  print('Welcome to the Brain Games!')
  gamer_name = prompt.string('May I have your name? ')
  print(f'Hello, {gamer_name}!')
  print(game_rules)

  for _ in range(ROUNDS_NUMBER):
    question, answer = generate_round()
    print(f'Question: {question}')
    your_answer = prompt.string('Your answer: ')

    if your_answer != answer:
      print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {gamer_name}!")
      return
    print('Correct!')
  
  print(f'Congratulations, {gamer_name}!')
