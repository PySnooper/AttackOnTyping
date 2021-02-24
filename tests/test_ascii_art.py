import io
import sys 
from ascii_art.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, lud_ascii, game_over_ascii, dev_menu_art, rules_art, thanks, you_win_ascii
import pytest


def test_welcome_message():
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    welcome_message()                               
    sys.stdout = sys.__stdout__                     
    print ('Captured', capturedOutput.getvalue())   
    actual = welcome_message()
    expected = 'By PySnooper'
    assert expected in actual

def test_lives():
    assert lives() == '♥ '

def test_easy_ascii():
    actual = len(easy_ascii())
    expected = 228
    assert actual == expected


def test_med_ascii():
    actual = len(med_ascii())
    expected = 306
    assert actual == expected


def test_hard_ascii():
    actual = len(hard_ascii())
    expected = 234
    assert actual == expected



def test_ext_ascii():
    actual = len(ext_ascii())
    expected = 466
    assert actual == expected


def test_lud_ascii():
    actual = len(lud_ascii())
    expected = 490
    assert actual == expected


def test_game_over_ascii():
    actual = len(game_over_ascii())
    expected = 484
    assert actual == expected


def test_dev_menu_art_ascii():
    actual = len(dev_menu_art())
    expected = 197
    assert actual == expected


def test_rules_art_ascii():
    actual = len(rules_art())
    expected = 215
    assert actual == expected


def test_thanks_ascii():
    actual = len(thanks())
    expected = 1264
    assert actual == expected

def test_you_win_ascii():
    actual = len(you_win_ascii())
    expected = 661
    assert actual == expected