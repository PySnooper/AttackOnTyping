from attackontyping.attackontyping import run_app, menu, game_over, about_us, print_rules, print_lives, print_points, dash_creator, check_points
from gamelogic.gamelogic import GameLogic
from ascii_art.ascii import game_over_ascii
import pytest
from io import StringIO

def test_menu(monkeypatch):
    input_mock = StringIO('a')
    monkeypatch.setattr('sys.stdin', input_mock)
    assert menu() == 'a'

def test_game_over(capsys):
    game = GameLogic()
    game_over(game)
    captured = capsys.readouterr()
    assert captured.out == game_over_ascii() + "\n"

# Start here please:
# def test_rules(capsys):
#     pass

# def test_print_lives():
#     pass

# def test_print_points():
#     pass








def test_check_points():
    game = GameLogic()
    game.points = 20
    returned_game = check_points(game)
    actual = game.diff
    expected = game.med_mode
    assert actual == expected

def test_dash():
    word = 'This is a test to see how many dashes are created.'
    actual = dash_creator(word)
    expected = '--------------------'
    assert actual == expected

def test_dash2():
    word = 'This is a test'
    actual = dash_creator(word)
    expected = '--------------'
    assert actual == expected