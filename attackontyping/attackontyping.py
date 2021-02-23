import time
import random
import os
import pyfiglet
from gamelogic.gamelogic import GameLogic
from colorama import Fore, Back, Style
from timer.timer import Timer
from ascii_art.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii, dev_menu_art, rules_art, thanks
from about.about import logan, anthony, nick, nebiyu

clear = lambda: os.system('clear')

# We should always default to this function, this is our controller
def run_app():
    clear()
    print(welcome_message())
    input('Press enter to begin.')
    clear()
    while True:
        user_input = menu()     
        if user_input == 'r':
            print_rules()     
        if user_input == 'a':
            game = GameLogic()
            adventure(game)          
        # if user_input == 'e':
        #     exhibition()
        if user_input == 'd':
            about_us()   
        if user_input == 'q':
            clear()
            print(thanks())
            exit()

def menu():
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
    while user_input not in ['r', 'a', 'e', 'd', 'q']:
            user_input = menu()
    return user_input

def adventure(game):
    clear()
    while game.lives > 0 and game.diff:
        play_round(game)
        if game.points >= game.diff["point_cap"]:
            game.next_diff()
    if game.lives == 0:
        game_over_ascii()
    else:
        print('You win!') # add a you win ascii
    print("You gained "
        + Fore.MAGENTA
        + str(game.points)
        + Style.RESET_ALL
        + " points. \n\nWould you like to try again?\n")
    user_input = input('(Y)es or (N)o \n\n> ').lower()
    if user_input == 'y':
        game.reset_game()
        adventure(game)
        
def play_round(game):
        timekeeper = Timer()
        text = game.get_text()
        if game.diff["warning"]:
            print(game.diff["warning"])
        
        print_lives(game)
        print_points(game)
        print(game.diff["ascii"]())
    
        print(f'You will have {game.diff["seconds"]} seconds to type what you see next. \n')

        dash_creator = lambda: print("-" * len(text)) # restrict this to a certain amount during extreme mode
        input('Press enter to begin\n')
        dash_creator()
        print(Fore.CYAN + text + Style.RESET_ALL)
        dash_creator()
        timekeeper.start()
        answer = input('\n> ')
        time_stop = timekeeper.stop()
        color = Fore.GREEN if answer == text else Fore.RED
        print(f"\nElapsed time: {time_stop:0.4f} seconds, you typed: "
            + color
            + (answer or 'None')
            + Style.RESET_ALL)
        if answer != text or time_stop > game.diff["seconds"]:
            print('')
            game.lives -= 1
            if game.lives > 0:
                print('Try again')
                print_lives(game)
                print('')
                input('Press enter for next round.')
                clear()

        else:
            game.points += game.diff["points_per"]
            print(f'Great work! You have {game.points} points! \n')
            input('Press enter for next round.')
            clear()

def game_over(game):
        clear()
        print(game_over_ascii())
       
def about_us():
    clear()
    print(dev_menu_art())
    about_us_menu()

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
            return
        else:
            about_us()

def print_rules():
        clear()
        print(rules_art())

        print(Fore.YELLOW 
        + "Adventure Mode:\n"
        + Style.RESET_ALL
        + "This console typing game app to bringing you high quality, \nfun and interactive free typing games, our typing game has \nfour difficulty levels starting from easy mode – extreme mode \nit grows up progressively. The game also has real time scoreboard, \nand you can always see where you are at which mode. \n\nYou motivate some to type faster, type more accurately, and enjoy playing our typing games!!" + 
        "\n\n- The game has 4 different difficulty levels easy-mode, medium-mode, hard-mode, and extremely-mode. Each level has 3 lives." + 
        "\n\n- Player has access to choose and play any difficulty level." + 
        "\n\n- If the player types and finished the words 3 times under each level at a given second got the score and transfer the next difficulty level. If not, the player gets a chance to play again." + 
        "\n\n- Every player has always can see the score, lives and difficulty level too. \n\n")
        user_input = input("\nPress enter to go back")
        return user_input

def print_lives(game):
    print('LIVES: ' 
        + Fore.RED 
        + f'{lives() * game.lives}' 
        + Style.RESET_ALL)

def print_points(game):
    print('POINTS: ' 
        + Fore.MAGENTA 
        + str(game.points) 
        + Style.RESET_ALL)

if __name__ == '__main__':
    run_app()