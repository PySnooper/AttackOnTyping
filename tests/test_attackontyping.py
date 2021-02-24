from attackontyping.attackontyping import run_app, menu, game_over, print_rules, print_lives, print_points, print_about_menu, about_us
from gamelogic.gamelogic import GameLogic
from ascii_art.ascii import game_over_ascii, thanks
from about.about import logan, anthony, nick, nebiyu
import pytest
from io import StringIO

def test_menu(mocker):
    mocker.patch('builtins.input', side_effect=['z','a'])
    assert menu() == 'a'

def test_game_over(capsys):
    game = GameLogic()
    game_over(game)
    captured = capsys.readouterr()
    assert captured.out == game_over_ascii() + "\n"

# Start here please:
def test_rules(capsys):
    pass

def test_print_lives():
    pass

def test_print_points():
    pass


def test_print_about_menu(devs, capsys):
    print_about_menu(devs)
    captured = capsys.readouterr()
    assert len(captured.out) == 93


def test_run_app(mocker):
    # '' Press enter at welcome
    # 'r' Go to rules
    # '' Go back
    # '' Go to devs
    # '1' Go t first dev
    # 'x' Back dev input
    # '0' Exit devs
    #  'q' quit app
    user_inputs = ['','r', '', 'd', '1', 'x', '0', 'q']

    with pytest.raises(SystemExit):
        mocker.patch('builtins.input', side_effect=user_inputs)
        run_app()


@pytest.fixture()
def devs():
    return {
        '1': {'name': 'Anthony Beaver', 'method': anthony},
        '2': {'name': 'Nick Dorkins', 'method': nick},
        '3': {'name': 'Logan Jones', 'method': logan},
        '4': {'name': 'Nebiuy Kifle', 'method': nebiyu}
        }