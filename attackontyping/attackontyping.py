import time
import random

from random_text import RandomText

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
                self.rules()
            if user_input == 'p':
                print('Selected play')
                self.play_game()
            if user_input == 'd':
                print('Selected devs')
                self.about_us()
            if user_input == 'e':
                print('Thanks for playing!')
                exit()
            # if user_input == 'ludacris':
            #     print('You\'re CRAZY!')
            #     self.start_ludacris_round()

    def rules(self):
        # color selector:
        # green = '\033[32;1;40m'
        # print(green + 'Game Rules')
        txt = 'Game Rules'
        center_txt = txt.center(110)
        print(green + center_txt)

        print("""
                Brief introduction:
        what the object of the game is and perhaps a funny intro to the game for party games

        """)
        self.menu_selection()


    def about_us(self):
        # about_us(self= None)
        # green = '\033[32;1;40m'
        # txt = 'About Us'
        # center_txt = txt.center(110)
        # print(green + center_txt )
        option = None

        # while option != 0:
        print("[1] Anthony Beaver")
        print("[2] Nick Dorkins")
        print("[3] Logan Jones")
        print("[4] Nebiuy Kifle")
        print("[0] Go to game page")
        option = int(input("enter index number: "))
        # green = '\033[32;1;40m'
        # print(green + 'about us')
        if option == 1:
            print("""
#################################################################################################################################################################################
        Anthony Beaver:
My about me: "Anthony Beaver is a full stack software developer from Seattle Washington.Passionate about problem solving and playing the drums! Looking to change the world one syntax error at a time..
#################################################################################################################################################################################
            """)
            self.about_us()
        elif option == 2:
            print("""
#################################################################################################################################################################################
            Nick Dorkins:
Software Developer with a background in Specialized Industrial Safety, and fabrication. Enjoy's traveling and spending time with family and puppies. Favorite things to do outside quarantine are going to Disney parks and playing Magic the Gathering.
#################################################################################################################################################################################
            """)
            self.about_us()
        elif option == 3:
            print("""
#################################################################################################################################################################################
            Logan Jones:
Logan Jones is a former product manager and current software engineer. She is a skilled problem solver who loves cats, taco bell, and world of warcraft..
#################################################################################################################################################################################
            """)
            self.about_us()
        elif option == 4:
            print("""
#################################################################################################################################################################################
            Nebiuy Kifle:
Hello My name is Nebiyu kifle. I am a professional and highly motivated software engineer.I have a background on marketing and logistics management for about 6 years back home in Ethiopia. I used to also have my own business.  I have worked on multiple projects and have a broad experience in software development at code fellows. I am passionate about to learn new think in techs industry. I would love the opportunity to put my experience at tech company. I am currently looking for a new role that will utilize my skills and experience and take my career to the next level.
#################################################################################################################################################################################
            """)
            self.about_us()
        elif option == 0:
            self.menu_selection()
        else:
            print("\nPlease enter a valid option\n")
            self.about_us()


# GAME LOGIC STUFF #

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
        while self.points < 20 and self.lives > 0:
            user_time = self.start_easy_round()
            # Easy mode: time allowed is 10, points per round 5
            self.calc_score(user_time, 15, 10)
            
        while self.points < 40 and self.lives > 0:
            self.difficulty = 'Medium'
            # Med round: time allowed is 10, points per round 10
            user_time = self.start_med_round()
            self.calc_score(user_time, 10, 10)

        while self.points < 60 and self.lives > 0:
            self.difficulty = 'Hard'
            user_time = self.start_hard_round()
            self.calc_score(user_time, 20, 10)
            # self.start_hard_round()

        while self.lives > 0:
            self.difficulty = 'Extreme'
            user_time = self.start_extreme_round()
            self.calc_score(user_time, 25, 10)
            # self.start_extreme_round()

        print(f'Game Over! You gained {self.points} points. \n Would you like to try again?')
        user_input = input('(Y)es or (N)o \n> ').lower()
        if user_input == 'y':
            self.points = 0
            self.lives = 3
            self.play_game()
        if user_input == 'n':
            exit()

    def start_easy_round(self):
        timekeeper = Timer()
        text = RandomText()
        question = text.get_words(1)
        print('EASY MODE!')
        print("Type the following words within 15 seconds:")
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
        timekeeper = Timer()
        text = RandomText()
        question = text.get_words(3)
        print('MEDIUM MODE!')
        print("Type the following sentence within 10 seconds:")
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

    def start_hard_round(self):
        timekeeper = Timer()
        text = RandomText()
        words = random.randrange(3, 5)
        question = text.get_sentences(1, words)
        print('HARD MODE!')
        print('********************************************')
        print('You now have capital letters and punctuation')
        print('********************************************')
        time.sleep(3)
        print("Type the following sentence within 20 seconds:")
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
        

    def start_extreme_round(self):
        timekeeper = Timer()
        text = RandomText()
        words = random.randrange(3, 6)
        sentence1 = text.get_sentences(1, words)
        words = random.randrange(3, 6)
        sentence2 = text.get_sentences(1, words)
        words = random.randrange(3, 6)
        sentence3 = text.get_sentences(1, words)
        question = f'{sentence1} {sentence2} {sentence3}'
        print('EXTREME MODE!')
        print('***********************************************************************')
        print('You now have capital letters, punctuation, and random length sentences!')
        print('***********************************************************************')
        time.sleep(3)
        print("Type the following sentence within 25 seconds:")
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
        
    # def start_ludacris_round(self):
    #     timekeeper = Timer()
    #     text = RandomText()
    #     words = random.randrange(7, 10)
    #     sentence1 = text.get_sentences(1, words)
    #     words = random.randrange(7, 10)
    #     sentence2 = text.get_sentences(1, words)
    #     words = random.randrange(7, 10)
    #     sentence3 = text.get_sentences(1, words)
    #     question = f'{sentence1} {sentence2} {sentence3}'
    #     print('LUDACRIS MODE!')
    #     print('***********************************************************************')
    #     print('You must be crazy to play this mode!')
    #     print('***********************************************************************')
    #     time.sleep(3)
    #     print("Type the following madness within 1 minute:")
    #     print("-------------------------")
    #     print(f'{question}')
    #     print("-------------------------")
    #     time.sleep(3)
    #     print('Ready..?')
    #     time.sleep(1)
    #     timekeeper.start()
    #     answer = input('Start!\n> ')
    #     time_stop = timekeeper.stop()
    #     print(f"Elapsed time: {time_stop:0.4f} seconds, you typed: {answer}")

    #     if answer != question:
    #         time_stop = 100
    #         return time_stop
    #     return time_stop

    





























if __name__ == '__main__':
    game = Game()
    game.menu_selection()