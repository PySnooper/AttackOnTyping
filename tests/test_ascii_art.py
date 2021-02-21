import io
import sys 
from ascii_art.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, lud_ascii, game_over_ascii, dev_menu_art, rules_art, thanks
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
    pass


def test_med_ascii():
    pass


def test_hard_ascii():
    pass



def test_ext_ascii():
    pass


def test_lud_ascii():
    pass




# @pytest.fixture



