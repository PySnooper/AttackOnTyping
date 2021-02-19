import time
import random
import os
import pyfiglet
from colorama import Fore, Back, Style
from random_text import RandomText
from timer import Timer
from ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii

# Function for clearing the console:
clear = lambda: os.system('clear')

class Game:

    def __init__(self):
        self.lives = 3
        self.points = 0
        self.easy_mode = {"descr": "EASY MODE", "words": 1, "seconds": "15", "struct": "words"}
        self.med_mode = {"descr": "MEDIUM MODE", "words": 3, "seconds": "10", "struct": "words"}
        self.hard_mode = {"descr": "HARD MODE", "words": 3, "seconds": "20", "struct": "sentences", "sentences" : 1}
        self.ext_mode = {"descr": "EXTREME MODE", "words": 4, "seconds": "15", "struct": "sentences", "sentences" : 3}


    @staticmethod
    def print_welcome():
        clear()
        welcome_message()

    @staticmethod
    def thanks_for_playing():
        print('\nThanks for playing!')
        exit()

    def start_app(self):
        self.print_welcome()
        time.sleep(1)
        input('Press enter to begin.')
        clear()
        self.menu_selection()

    def menu_selection(self):
        print("Welcome to Attack on Typing!")
        play = 'Would you like to: \n(P)lay the game \n(R)ead the rules \n(D)ev Bios \n(Q)uit?'
        user_input = input(play + '\n'+ '> ').lower()
        
        if user_input == 'r':
            self.rules()
        if user_input == 'p':
            self.play_game()
        if user_input == 'd':
            self.about_us()
        if user_input == 'q':
            self.thanks_for_playing()

    def rules(self):
        txt = 'Game Rules'
        center_txt = txt.center(110)
        print(green + center_txt)

        print("""
                Brief introduction:
        what the object of the game is and perhaps a funny intro to the game for party games

        """)
        self.menu_selection()


# GAME LOGIC STUFF #
    # Calcuation logic:
    def end_round(self, user_time, time_allowed, points):
        if user_time < time_allowed:
            self.points += points
            print(f'Great work! You have {self.points} points! \n')
            print('Get ready for the next question!\n')
            time.sleep(2)
            clear()
        else:
            print('')
            self.lives -= 1
            if self.lives > 0:
                print('Try again')
                print(f'Lives left: {self.lives}!')
                print('')
                time.sleep(2)
                clear()

    # Adventure game loop conditionals:
    def play_game(self):
        clear()
        while self.points < 20 and self.lives > 0:
            self.difficulty = 'Easy'
            user_time = self.start_round(self.easy_mode)
            # Easy mode: time allowed is 10, points per round 5
            self.end_round(user_time, 15, 10)
            
        while self.points < 40 and self.lives > 0:
            # Med round: time allowed is 10, points per round 10
            user_time = self.start_round(self.med_mode)
            self.end_round(user_time, 10, 10)

        while self.points < 60 and self.lives > 0:
            user_time = self.start_round(self.hard_mode)
            self.end_round(user_time, 20, 10)

        while self.points >= 60 and self.lives > 0:
            user_time = self.start_round(self.ext_mode)
            self.end_round(user_time, 25, 10)

        # Game over stuff here:
        clear()
        game_over_ascii()
        print(f'You gained {self.points} points. \n Would you like to try again?')
        user_input = input('(Y)es or (N)o \n> ').lower()
        if user_input == 'y':
            self.points = 0
            self.lives = 3
            self.play_game()
        if user_input == 'n':
            exit()
   
    # Print functions
    @staticmethod
    def print_hard_ascii():
        print('********************************************')
        print('You now have capital letters and punctuation')
        print('********************************************')

    @staticmethod
    def print_ext_ascii():
        print('***********************************************************************')
        print('You now have capital letters, punctuation, and random length sentences!')
        print('***********************************************************************')
    
    # Modular game round logic:
    def start_round(self, mode):
        timekeeper = Timer()
        text = RandomText()
        if mode["struct"] == 'words':
            question = text.get_words(mode["words"])
        if mode["struct"] == 'sentences':
            question = text.get_sentences(mode["sentences"], mode["words"], True)
        if mode["descr"] == "HARD MODE":
                self.print_hard_ascii()
        if mode["descr"] == "EXTREME MODE":
            self.print_ext_ascii()

        # Printing the red hearts representing the player's lives:
        print('LIVES: ' + Fore.RED + f'{lives() * self.lives}' + Style.RESET_ALL)
        if mode['descr'] == 'EASY MODE':
            easy_ascii()
        if mode['descr'] == 'MEDIUM MODE':
            med_ascii()
        if mode['descr'] == 'HARD MODE':
            hard_ascii()
        if mode['descr'] == 'EXTREME MODE':
            ext_ascii()

        print(f'You will have {mode["seconds"]} seconds to type what you see next. \n')

        #ascii art here:
        dash_creator = lambda: print("-" * len(question))
        input('Press enter to begin')
        dash_creator()
        print(f'{question}')
        dash_creator()
        timekeeper.start()
        answer = input('> ')
        time_stop = timekeeper.stop()
        print(f"Elapsed time: {time_stop:0.4f} seconds, you typed: {answer}")
        if answer != question:
            time_stop = 100
            return time_stop
        return time_stop

    def about_us(self):
        option = None

        # while option != 0:
        print("[1] Anthony Beaver")
        print("[2] Nick Dorkins")
        print("[3] Logan Jones")
        print("[4] Nebiuy Kifle")
        print("[0] Go to game page")
        option = int(input("enter index number: "))
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



























if __name__ == '__main__':
    game = Game()
    game.start_app()