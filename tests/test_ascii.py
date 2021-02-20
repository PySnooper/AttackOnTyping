from attackontyping.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii, dev_menu_art, rules_art, thanks
import pytest 

def test_easy_ascii():
    actual = easy_ascii()
    expected = """ \
    ***************************\ 
     _____    _    ______   __\
    | ____|  / \  / ___\ \ / /\
    |  _|   / _ \ \___ \\ V / \
    | |___ / ___ \ ___) || |  \
    |_____/_/   \_\____/ |_|  \
                              \
    ***************************\
    """
    assert actual == expected

def test_heart_ascii():
    actual = lives()
    expected = "♥ "
    assert actual == expected