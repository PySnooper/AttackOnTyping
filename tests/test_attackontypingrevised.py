from attackontyping.attackontypingrevised import GameLogic, easy_mode, med_mode, hard_mode, ext_mode
import pytest

def test_reset_game(game):
    game.lives = 100
    game.points = 100
    game.diff = ext_mode
    game.reset_game()
    assert game.lives == 3
    assert game.points == 0
    assert game.diff == easy_mode

def test_next_diff(game):
    game.next_diff()
    assert game.diff == med_mode

def test_next_diff_till_none(game):
    game.next_diff()
    game.next_diff()
    game.next_diff()
    game.next_diff()
    assert game.diff == None

def test_text_words(game):
    game.diff = med_mode 
    words = game.get_text()
    actual = len(words.split(' '))
    expected = game.diff["words"]
    assert actual == expected

def test_text_sentence(game):
    game.diff = hard_mode 
    sentence = game.get_text()
    actual = len(sentence.split('. '))
    expected = game.diff["sentences"]
    assert actual == expected


@pytest.fixture
def game():
    return GameLogic()