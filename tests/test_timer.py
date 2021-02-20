import pytest
import time
from timer.timer import Timer, TimerError

def test_timer(timer):
    timer.start()
    time.sleep(1)
    stopper = timer.stop()
    actual = int(stopper)
    expected = 1
    assert actual == expected

def test_timer_start_exception(timer):
    timer.start()
    with pytest.raises(TimerError):
        timer.start()

def test_timer_stop_exception(timer):
    with pytest.raises(TimerError):
        timer.stop()


@pytest.fixture()
def timer():
    return Timer()