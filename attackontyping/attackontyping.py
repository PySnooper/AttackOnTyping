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
            if user_input == 'd':
                print('Selected devs')
            if user_input == 'e':
                print('Thanks for playing!')
                exit()


    def rules(self):
        pass










    def about_us(self):
        pass









    def play_game(self):
        # easy - extreme rounds in here   
        pass








    def start_easy_round(self):
        pass







    def start_med_round(self):
        pass








    def start_hard_round(self):
        pass









    def start_extreme_round(self):
        pass
































if __name__ == '__main__':
    game = Game()
    game.menu_selection()