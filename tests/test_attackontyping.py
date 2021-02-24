import io
import sys 
from attackontyping.attackontyping import run_app, menu, game_over, about_us, print_rules, print_lives, print_points
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
def test_rules(monkeypatch):
    # print_rules()
    input_mock = StringIO('\n')
    monkeypatch.setattr('sys.stdin', input_mock)
    expected ='Adventure Mode:'
    assert print_rules() == ''


def test_print_lives(capsys):
    game = GameLogic()
    print_lives(game)
    captured = capsys.readouterr()
    expected = '♥'
    assert expected in captured.out

def test_print_points(capsys):
    game = GameLogic()
    print_points(game)
    captured = capsys.readouterr()
    expected = 'POINTS'
    assert expected in captured.out 