import time
import random
import os
import pyfiglet
from colorama import Fore, Back, Style
from random_text import RandomText
from timer import Timer
from ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii, dev_menu_art, rules_art, thanks
from about import logan, anthony, nick, nebiyu

clear = lambda: os.system('clear')

class Game:

    def __init__(self):
        self.lives = 3
        self.points = 0
        self.easy_mode = {"descr": "EASY MODE", "words": 1, "seconds": "15", "struct": "words"}
        self.med_mode = {"descr": "MEDIUM MODE", "words": 3, "seconds": "10", "struct": "words"}
        self.hard_mode = {"descr": "HARD MODE", "words": 3, "seconds": "20", "struct": "sentences", "sentences" : 1}
        self.ext_mode = {"descr": "EXTREME MODE", "words": 4, "seconds": "25", "struct": "sentences", "sentences" : 3}

    def reset_game(self):
        self.lives = 3
        self.points = 0

    @staticmethod
    def print_welcome():
        clear()
        welcome_message()

    @staticmethod
    def thanks_for_playing():
        clear()
        thanks()
        exit()

    def start_app(self):
        clear()
        self.print_welcome()
        time.sleep(1)
        input('Press enter to begin.')
        clear()
        self.menu_selection()

    def menu_selection(self):
        clear()
        print("Welcome to " 
            + Fore.GREEN 
            + "Attack "
            + Fore.RED 
            + "on "
            + Fore.BLUE 
            + "Typing"
            + Style.RESET_ALL
            + "!\n")
        play = 'Would you like to: \n\n(A)dventure Mode \n(E)xhibition Mode \n(R)ead the rules \n(D)ev Bios \n(Q)uit'
        user_input = input(play + '\n\n'+ '> ').lower()
        
        if user_input == 'r':
            self.rules()
        if user_input == 'a':
            self.play_game()
        if user_input == 'e':
            self.exhibition_game()
        if user_input == 'd':
            self.about_us()
        if user_input == 'q':
            self.thanks_for_playing()
        self.menu_selection()

    def rules(self):
        clear()
        rules_art()
        print(Fore.YELLOW 
        + "Adventure Mode:\n"
        + Style.RESET_ALL
        + "Progress through Easy, Medium, Hard, and Extreme\ndifficulties by typing text as fast as you can! You'll lose a life if you type incorrectly or run out of time.\n\n")
        
        print(Fore.MAGENTA
        + "Exhibition Mode:\n"
        + Style.RESET_ALL
        + "Start your game at a specific difficulty!")
        input("\nPress enter to go back")
        self.menu_selection()

    def end_round(self, user_time, time_allowed, points):
        if user_time < time_allowed:
            self.points += points
            print(f'Great work! You have {self.points} points! \n')
            print('Get ready for the next round!\n')
            time.sleep(2)
            clear()
        else:
            print('')
            self.lives -= 1
            if self.lives > 0:
                print('Try again')
                self.print_lives()
                print('')
                time.sleep(2)
                clear()

    def play_game(self):
        clear()
        self.reset_game()
        while self.points < 20 and self.lives > 0:
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
            
        self.game_over(self.play_game)
    
    def game_over(self, game_func):
        clear()
        game_over_ascii()
        print("You gained "
        + Fore.MAGENTA
        + str(self.points)
        + Style.RESET_ALL
        + " points. \n\nWould you like to try again?\n")
        user_input = input('(Y)es or (N)o \n\n> ').lower()
        if user_input == 'y':
            game_func()
        if user_input == 'n':
            self.menu_selection()

    def exhibition_game(self):
        clear()
        self.reset_game()
        print('Here you will play one difficulty until you\'re out of lives. \n')

        user_input = input('Would you like to play \n(E)asy \n(M)edium \n(H)ard \n(X)treme \n(R)eturn to main menu \n> ').lower()
        clear()
        print('Play until you run out of lives.')
        if user_input == 'e':
            while self.lives > 0:
                user_time = self.start_round(self.easy_mode)
                self.end_round(user_time, 15, 10)   
            self.game_over(self.exhibition_game)
        if user_input == 'm':
            while self.lives > 0:
                user_time = self.start_round(self.med_mode)
                self.end_round(user_time, 10, 10)  
            self.game_over(self.exhibition_game) 
        if user_input == 'h':
            while self.lives > 0:
                user_time = self.start_round(self.hard_mode)
                self.end_round(user_time, 20, 10)
            self.game_over(self.exhibition_game)
        if user_input == 'x':
            while self.lives > 0:
                user_time = self.start_round(self.ext_mode)
                self.end_round(user_time, 25, 10)
            self.game_over(self.exhibition_game)
        if user_input == 'r':
            self.menu_selection()
        
    @staticmethod
    def print_hard_ascii():
        print('********************************************')
        print(Fore.YELLOW 
            + 'You now have capital letters and punctuation'
            + Style.RESET_ALL )
        print('********************************************\n')

    @staticmethod
    def print_ext_ascii():
        print('***********************************************************************')
        print(Fore.YELLOW 
            + 'You now have capital letters, punctuation, and random length sentences!'
            + Style.RESET_ALL)
        print('***********************************************************************\n')
    
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

        self.print_lives()
        self.print_points()
        if mode['descr'] == 'EASY MODE':
            easy_ascii()
        if mode['descr'] == 'MEDIUM MODE':
            med_ascii()
        if mode['descr'] == 'HARD MODE':
            hard_ascii()
        if mode['descr'] == 'EXTREME MODE':
            ext_ascii()

        print(f'You will have {mode["seconds"]} seconds to type what you see next. \n')

        dash_creator = lambda: print("-" * len(question))
        input('Press enter to begin\n')
        dash_creator()
        print(Fore.CYAN + question + Style.RESET_ALL)
        dash_creator()
        timekeeper.start()
        answer = input('\n> ')
        time_stop = timekeeper.stop()
        color = Fore.GREEN if answer == question else Fore.RED
        print(f"\nElapsed time: {time_stop:0.4f} seconds, you typed: "
            + color
            + (answer or 'None')
            + Style.RESET_ALL)
        if answer != question:
            time_stop = 100
            return time_stop
        return time_stop

    def about_us(self):
        option = None
        clear()
        dev_menu_art()

        def about_us_menu():
            print("(1) Anthony Beaver")
            print("(2) Nick Dorkins")
            print("(3) Logan Jones")
            print("(4) Nebiuy Kifle")
            print("(0) Go to game page")
            option = input("\nSelect a developer:\n> ")
            
            if option == '1':
                clear()
                anthony()
                print('\n')
                about_us_menu()
            elif option == '2':
                clear()
                nick()
                print('\n')
                about_us_menu()
            elif option == '3':
                clear()
                logan()
                print('\n')
                about_us_menu()
            elif option == '4':
                clear()
                nebiyu()
                print('\n')
                about_us_menu()
            elif option == '0':
                self.menu_selection()
            else:
                self.about_us()

        about_us_menu()

    def print_lives(self):
        print('LIVES: ' 
            + Fore.RED 
            + f'{lives() * self.lives}' 
            + Style.RESET_ALL)

    def print_points(self):
        print('POINTS: ' 
            + Fore.MAGENTA 
            + str(self.points) 
            + Style.RESET_ALL)

if __name__ == '__main__':
    game = Game()
    game.start_app()