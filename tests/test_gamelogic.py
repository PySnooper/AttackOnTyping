from gamelogic.gamelogic import GameLogic
import pytest

def test_reset_game(game):
    game.lives = 100
    game.points = 100
    game.diff = game.ext_mode
    game.reset_game()
    assert game.lives == 3
    assert game.points == 0
    assert game.diff == game.easy_mode

def test_next_diff(game):
    game.next_diff()
    assert game.diff == game.med_mode

def test_next_diff_till_none(game):
    game.next_diff()
    game.next_diff()
    game.next_diff()
    game.next_diff()
    assert game.diff == None

def test_text_words(game):
    game.diff = game.med_mode 
    words = game.get_text()
    actual = len(words.split(' '))
    expected = game.diff["words"]
    assert actual == expected

def test_text_sentence(game):
    game.diff = game.hard_mode 
    sentence = game.get_text()
    actual = len(sentence.split('. '))
    expected = game.diff["sentences"]
    assert actual == expected

def test_set_diff(game):
    difficulty = game.hard_mode
    game.set_diff(difficulty)
    actual = game.diff["descr"]
    expected = game.hard_mode["descr"]
    assert actual == expected

@pytest.fixture
def game():
    return GameLogic()