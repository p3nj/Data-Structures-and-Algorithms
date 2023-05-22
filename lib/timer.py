import time
from utils import headlines


class Timer:
    def __init__(self, toggle=False, name=''):
        self.toggle = toggle
        self.name = name

    def stopwatch(self):

        def mark_start():
            global start_time
            start_time = time.perf_counter()

        def mark_stop():
            global stop_time
            stop_time = time.perf_counter()

        if self.toggle:
            mark_start()
            headlines("{}...".format(self.name), '=')
        else:
            mark_stop()
            headlines("Elapsed: {} Seconds".format(stop_time - start_time), '-')
