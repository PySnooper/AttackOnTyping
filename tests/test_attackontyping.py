from attackontyping.attackontyping import Game
import pytest 



#  TODO  Test game methods

def test_reset_game(game):
    game.lives = 100
    game.points = 100
    game.reset_game()
    assert game.lives == 3
    assert game.points == 0

#  TODO  Test Mode method

def test_easy_ascii(game):
    pass
    
#  TODO  Test Scoring method

#  



@pytest.fixture
def game():
    return Game()