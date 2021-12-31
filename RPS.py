# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
import random
ScoreAi = 0
ScorePlayer = 0
while True:
  print('Hi player one, You can either be')
  print('1) Rock')
  print('2) Paper')
  print('3) Scissors')
  PlayerOne = int(input('Pick 1, 2, or 3. '))
  Computer = random.randint(1,3)
  print('The Computer chose ' + str(Computer))
  if PlayerOne == Computer:
    print('It is a tie!')
    ScoreAi = ScoreAi + 1
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 1 and Computer == 2:
    print(' Computers Paper beats your rock! You lose! ')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 1 and Computer == 3:
    print('Your Rock beats Computers scissors! You win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 2 and Computer == 3:
    print('Computers Scissors beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  elif PlayerOne == 2 and Computer == 1:
    print('Your Paper beats Computers rock! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 2:
    print('Your Scissors beats Computers paper! You Win!')
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 3 and Computer == 1:
    print('Computers Rock beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
  print('Do you want to keep playing?')
  print('1) Yes')
  print('2) No')
  Choice = input('Choose 1 or 2.')

  if Choice == '2':
    print('You won ' + str(ScorePlayer) + ' games and the computer won ' + str(ScoreAi) + ' games.')
    if ScorePlayer > ScoreAi:
      print('Congratulations! You win!')
    elif ScorePlayer < ScoreAi:
      print('The computer won most of the games. You lose!')
    else:
      print('Tie!')
    print('Thank you for playing!')
    break