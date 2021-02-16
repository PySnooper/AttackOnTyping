import random
# from faker import Faker

# fake = Faker()
# Faker.seed(0)

# questions = []

# for _ in range(5):
#   print(fake.sentences)
#   questions.append(fake.sentences)

# print(questions[0])

questions = ['Typing is fun', 'I can type everything', 'You can type many words', 'How many tries are you on', 'This is my favorite game', 'Taco sauce is tasty']

hash_10 = """
██╗ ██╗ ██╗ ██╗ ██╗ ██╗    ██╗ ██╗ ██╗ ██╗ ██╗ ██╗ 
╚██╗╚██╗╚██╗╚██╗╚██╗╚██╗  ██╔╝██╔╝██╔╝██╔╝██╔╝██╔╝
 ╚██╗╚██╗╚██╗╚██╗╚██╗╚██╗██╔╝██╔╝██╔╝██╔╝██╔╝██╔╝
 ██╔╝██╔╝██╔╝██╔╝██╔╝██╔╝╚██╗╚██╗╚██╗╚██╗╚██╗╚██╗
██╔╝██╔╝██╔╝██╔╝██╔╝██╔╝  ╚██╗╚██╗╚██╗╚██╗╚██╗╚██╗
╚═╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝    ╚═╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝ ╚═╝
"""
welcome_message = 'Welcome to Attack on Typing!'
welcome_message = """ █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗ 
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝ 
███████║   ██║      ██║   ███████║██║     █████╔╝  
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗  
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗ 
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 
                 ██████╗ ███╗   ██╗                
                ██╔═══██╗████╗  ██║                
█████╗█████╗    ██║   ██║██╔██╗ ██║    █████╗█████╗
╚════╝╚════╝    ██║   ██║██║╚██╗██║    ╚════╝╚════╝
                ╚██████╔╝██║ ╚████║                
                 ╚═════╝ ╚═╝  ╚═══╝                
 ████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗    
 ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝    
    ██║    ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗   
    ██║     ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║   
    ██║      ██║   ██║     ██║██║ ╚████║╚██████╔╝   
    ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝"""
# get_ready = print('Get ready for the next question!\n')

import time

## Time keeping logic
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
      self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed_time

## Menu selection and rules
def entry():
  print(hash_10)
  print(welcome_message)
  print(hash_10)
  print('Would you like to review the rules, play the game Or exit?:')
  play_or_rules = input('R for rules, G for game, and exit to leave \n').upper()
  if play_or_rules == 'R':
    rules()
  elif play_or_rules == 'G':
    game()
  else:
    print('Thanks for playing!')
    return

def rules():
  print(hash_10)
  print("When the game says 'Start!' then start typing. \n")
  print('You have a limited amount of tries to type in the sentence you have been givin. \n')
  print('The sentence must be spelled exactly how it was printed! \n')
  print('Once you get enough points the sentences will become more difficult to type.')
  print('would you like to play or return to the main menu?')
  play_or_entry = input('R for return, G for game \n').upper()
  if play_or_entry == 'R':
    entry()
  elif play_or_entry == 'G':
    game()

## Game logic


def get_timed_answer():
  timekeeper = Timer()
  question = random.choice(questions)
  
  print("Type the following sentence:")
  print("-------------------------")
  print(f'{question} \n')
  print("-------------------------")
  time.sleep(3)
  print('Ready..?')
  time.sleep(1)
  timekeeper.start()
  answer = input('Start!\n')
  time_stop = timekeeper.stop()
  # print(time_stop)
  print(f"Elapsed time: {time_stop:0.4f} seconds, you typed: {answer}")
  if answer != question:
    time_stop = 100
    return time_stop
  return time_stop

def game():
  
  tries = 3
  points = 0
  while tries > 0:
    while points < 3 and tries > 0:
      ## Easy difficulty
      print(hash_10)
      print('Easy difficulty! 10 seconds to win!')
      print(hash_10)
      time_used = get_timed_answer()

      if time_used < 10:
        points += 1
        print(f'Great work! You have {points} points! \n')
        print('Get ready for the next question!\n')
        time.sleep(3)
      else:
        print('')
        print('Try again')
        tries -= 1
        print('tries left: ', tries)

    ## harder difficulty
    while points < 5 and tries > 0:
      print(hash_10)
      print('Harder difficulty! 5 seconds to win!')
      print(hash_10)
      time_used = get_timed_answer()

      if time_used < 5:
        points += 1
        print(f'Great work! You have {points} points! \n')
        if points < 5:
          print('Get ready for the next question!\n')
        time.sleep(3)
      else:
        print('Try again')
        tries -= 1
        print('tries left: ', tries)
    if points == 5:
      print(f'You win! You scored {points} points!')
      print('Try again?')
      try_again = input('Y for yes, N for no and exit \n').upper()
      if try_again == 'Y':
        game()
      else:
        return
  print(f'Total points: {points}, try again? \n')
  try_again = input('Y for yes, N for no and exit').upper()
  if try_again == 'Y':
    game()
  else:
    return


# timekeeper = Timer()

# timekeeper.start()
# time.sleep(2)
# timekeeper.stop()

entry()
# game()
      
