import time

class TimerError(Exception):
     
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
      self._start_time = None

    def start(self):
        """
        [Start a timer when the user starts a round of play.]

        Raises:
            TimerError: [Raises Error if the timer output and the stopped time are not the same - indicates that the timer did not stop at the end of the previous round]
 
        """        
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):

        """
        [Stop the timer, and report the elapsed time]

        Raises:
            TimerError: [Raises Error if the timer output and the stopped time are not the same - indicates that the timer did not stop at the end of the previous round]

        Returns:
            [float]: [Total time user took to complete/type the word challenge in seconds out to the fourth decimal place. (10,000th of a second)]
        """        
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed_time
