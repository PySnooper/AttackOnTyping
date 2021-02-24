import time
import random
import os
import pyfiglet
from gamelogic.gamelogic import GameLogic
from colorama import Fore, Back, Style
from timer.timer import Timer
from ascii_art.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii, dev_menu_art, rules_art, thanks, you_win_ascii
from about.about import logan, anthony, nick, nebiyu


def clear(): return os.system('clear')


devs = {
    '1': {'name': 'Anthony Beaver', 'method': anthony},
    '2': {'name': 'Nick Dorkins', 'method': nick},
    '3': {'name': 'Logan Jones', 'method': logan},
    '4': {'name': 'Nebiuy Kifle', 'method': nebiyu}
}


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
        if user_input == 'e':
            game = GameLogic()
            exhibition(game)
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
    user_input = input(play + '\n\n' + '> ').lower()
    while user_input not in ['r', 'a', 'e', 'd', 'q']:
        user_input = menu()
    return user_input


def adventure(game):
    clear()
    while game.lives > 0 and game.diff:
        clear()
        play_round(game)
        check_points(game)
    if game.lives == 0:
        user_input = game_over(game)
    else:
        clear()
        print(you_win_ascii())
        print("You gained "
        + Fore.MAGENTA
        + str(game.points)
        + Style.RESET_ALL
        + " points. \n\nWould you like to try again?\n")
        user_input = input('(Y)es or (N)o \n\n> ').lower()
    if user_input == 'y':
        game.reset_game()
        adventure(game)


def exhibition(game):
    clear()
    print("Choose your difficulty, play till you run out of lives.")
    user_input = input('Would you like to play \n(E)asy \n(M)edium \n(H)ard \n(X)treme \n(R)eturn to main menu \n> ').lower()
    clear()
    modes = {'e': game.easy_mode, 'm': game.med_mode, 'h': game.hard_mode, 'x': game.ext_mode}
    for i in modes:
        if user_input == i:
            game.diff = modes[i]
            while game.lives > 0:
                clear()
                play_round(game)
            user_input = game_over(game)
            if user_input == 'y':
                game.reset_game()
                exhibition(game)


def play_round(game):
        timekeeper = Timer()
        text = game.get_text()
        if game.diff["warning"]:
            print(game.diff["warning"])
        
        print_lives(game)
        print_points(game)
        print(game.diff["ascii"]())
    
        print(f'You will have {game.diff["seconds"]} seconds to type what you see next. \n')
        input('Press enter to begin\n')
        print(dash_creator(text))
        print(Fore.CYAN + text + Style.RESET_ALL)
        print(dash_creator(text))
        timekeeper.start()
        answer = input('\n> ')
        time_stop = timekeeper.stop()
        color = Fore.GREEN if answer == text else Fore.RED
        print(f"\nElapsed time: {time_stop:0.4f} seconds, you typed:\n"
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
            print_great_work(game)
            input('Press enter to continue\n')


def print_great_work(game):
    print('\nGreat work! You have '
        + Fore.MAGENTA
        + str(game.points)
        + Style.RESET_ALL
        + ' points!\n')


def game_over(game):
    clear()
    print(game_over_ascii())
    print("You gained "
    + Fore.MAGENTA
    + str(game.points)
    + Style.RESET_ALL
    + " points. \n\nWould you like to play again?\n")
    return input('(Y)es or (N)o \n\n> ').lower()


def about_us():
    clear()
    print(dev_menu_art())

    def about_menu_selection():
        print_about_menu(devs)
        option = input("\nSelect a developer:\n> ")

        if option in devs.keys():
            print_method = devs[option]['method']
            clear()
            print_method()
            about_menu_selection()
        elif option == '0':
            return
        else:
            about_us()
    about_menu_selection()


def print_about_menu(devs):
    for (key, value) in devs.items():
        print(f'({key})', value['name'])
    print("(0) Return to main menu")


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


def dash_creator(text):
    if len(text) > 70:
        to_print = ("-" * 70)
        return to_print
    to_print = ("-" * len(text))
    return to_print


def check_points(game):
    if game.points >= game.diff["point_cap"]:
        game.next_diff()
    return game


if __name__ == '__main__':
    run_app()