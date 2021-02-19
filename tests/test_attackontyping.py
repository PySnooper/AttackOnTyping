from attackontyping import __version__
from attackontyping.timer import Timer
# import pytest
import time

def test_version():
    assert __version__ == '0.1.0'

def test_timer():
    timer = Timer()
    timer.start()
    time.sleep(1)
    stopper = timer.stop()
    actual = int(stopper)
    expected = 1
    assert actual == expected

#  TODO  Test game methods
#  TODO  Test Mode method
#  TODO  Test Scoring method
