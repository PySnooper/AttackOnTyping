from attackontyping.attackontyping import run_app, menu, game_over, about_us, print_rules, print_lives, print_points, dash_creator, check_points, print_about_menu, print_great_work
import io
import sys 
from gamelogic.gamelogic import GameLogic
from ascii_art.ascii import game_over_ascii, thanks
from about.about import logan, anthony, nick, nebiyu
import pytest
from io import StringIO

def test_menu(mocker):
    mocker.patch('builtins.input', side_effect=['z','a'])
    assert menu() == 'a'

def test_game_over(monkeypatch, game):
    input_mock = StringIO('n')
    monkeypatch.setattr('sys.stdin', input_mock)
    assert game_over(game) == 'n'

def test_rules(monkeypatch):
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


def test_check_points():
    game = GameLogic()
    game.points = 20
    returned_game = check_points(game)
    actual = game.diff
    expected = game.med_mode
    assert actual == expected

def test_dash():
    word = 'This is a test to see how many dashes are created. Now how many words are there? No one could tell!'
    actual = dash_creator(word)
    expected = '----------------------------------------------------------------------'
    assert actual == expected

def test_dash2():
    word = 'This is a test'
    actual = dash_creator(word)
    expected = '--------------'
    assert actual == expected


def test_print_about_menu(devs, capsys):
    print_about_menu(devs)
    captured = capsys.readouterr()
    assert len(captured.out) == 93


def test_print_great_work(game, capsys):
    print_great_work(game)
    captured = capsys.readouterr()
    assert len(captured.out) == 42


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


def test_run_adventure_fail(mocker):
    user_inputs = ['', 'a', '', '', '', '', '', '', '', '', '', 'q']

    with pytest.raises(SystemExit):
        mocker.patch('builtins.input', side_effect=user_inputs)
        run_app()

def test_run_exhibition_fail(mocker):
    user_inputs = ['', 'e', 'x', '', '', '', '', '', '', '', '', '', 'q']

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

@pytest.fixture()
def game():
    return GameLogic()