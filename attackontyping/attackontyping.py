import time
import random

sentences = ['sentence one', 'sentence two', 'sentence three']

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

class Game:
    def __init__(self):
        self.lives = 3
        self.points = 0
        self.difficulty = 'easy'

    def menu_selection(self):
        # Print Welcome ASCII

        user_input = None

        while user_input not in ('r', 'p', 'd', 'e'):
            print('Would you like to (p)lay the game, read the (r)ules, learn about the (d)evs, or (e)xit?')
            
            user_input = input('> ').lower()
            
            if user_input == 'r':
                print('Selected rules')
            if user_input == 'p':
                print('Selected play')
                self.play_game()
            if user_input == 'd':
                print('Selected devs')
            if user_input == 'e':
                print('Thanks for playing!')
                exit()


    def rules(self):
        pass










    def about_us(self):
        pass




    # Calcuation logic:
    def calc_score(self, user_time, time_allowed, points):
        if user_time < time_allowed:
            self.points += points
            print(f'Great work! You have {self.points} points! \n')
            print('Get ready for the next question!\n')
            time.sleep(2)
        else:
            print('')
            print('Try again')
            self.lives -= 1
            print(f'Lives left: {self.lives}!')
            time.sleep(2)



    # Game logic starts here:
    def play_game(self):
        # easy - extreme rounds in here
        # while self.lives > 0:
        while self.points < 15 and self.lives > 0:
            user_time = self.start_easy_round()
            # Easy mode: time allowed is 10, points per round 5
            self.calc_score(user_time, 10, 5)
            
        while self.points < 45 and self.lives > 0:
            self.difficulty = 'Medium'
            # Med round: time allowed is 10, points per round 10
            # self.start_med_round()

        while self.points < 100 and self.lives > 0:
            self.difficulty = 'Hard'
            # self.start_hard_round()

        while self.points < 200 and self.lives > 0:
            self.difficulty = 'Extreme'
            # self.start_extreme_round()

        print(f'Game Over! You gained {self.points}. \n Would you like to try again?')
        user_input = input('(Y)es or (N)o \n> ').lower()
        if user_input == 'y':
            self.points = 0
            self.lives = 3
            self.play_game()
        if user_input == 'n':
            exit()
        # pass

    def start_easy_round(self):
        timekeeper = Timer()

        #Logan's words will replace this:
        question = random.choice(sentences)

        print("Type the following sentence:")
        print("-------------------------")
        print(f'{question}')
        print("-------------------------")
        time.sleep(3)
        print('Ready..?')
        time.sleep(1)
        timekeeper.start()
        answer = input('Start!\n> ')
        time_stop = timekeeper.stop()
        print(f"Elapsed time: {time_stop:0.4f} seconds, you typed: {answer}")
        if answer != question:
            time_stop = 100
            return time_stop
        return time_stop







    def start_med_round(self):
        pass








    def start_hard_round(self):
        pass









    def start_extreme_round(self):
        pass


    





























if __name__ == '__main__':
    game = Game()
    game.menu_selection()