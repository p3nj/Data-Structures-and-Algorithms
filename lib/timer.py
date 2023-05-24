import time
from utils import headlines


class Timer:
    def __init__(self, toggle=False, name=''):
        self.toggle = toggle
        self.name = name

    def stopwatch(self, silent=True):
        def mark_start():
            global start_time
            start_time = time.perf_counter()

        def mark_stop():
            global stop_time
            stop_time = time.perf_counter()

        if self.toggle:
            mark_start()
            if silent is not True:
                headlines("{}...".format(self.name), '=', end=False)
            return None

        else:
            mark_stop()
            if silent is not True:
                headlines("Elapsed: {} Seconds".format(stop_time - start_time), '=', end=True)
            return stop_time - start_time
