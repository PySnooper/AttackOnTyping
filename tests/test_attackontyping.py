from attackontyping.attackontyping import Game
import pytest
from colorama import Fore, Back, Style
# import sys


#  TODO Test game methods

def test_reset_game(game):
    game.lives = 100
    game.points = 100
    game.reset_game()
    assert game.lives == 3
    assert game.points == 0


def test_print_hard_ascii(capsys):
    game = Game()
    game.print_hard_ascii()
    captured = capsys.readouterr()
    string = '********************************************\n' \
        + Fore.YELLOW \
        + 'You now have capital letters and punctuation\n' \
        + Style.RESET_ALL \
        + '********************************************\n\n'
    assert captured.out == string

def test_print_ext_ascii(game, capsys):
    game.print_ext_ascii()
    captured = capsys.readouterr()
    string = '***********************************************************************' \
    + Fore.YELLOW \
    + 'You now have capital letters, punctuation, and random length sentences!' \
    + Style.RESET_ALL \
    + '***********************************************************************\n' \
    + '\n'

    assert captured.out == string


@pytest.fixture
def game():
    return Game()