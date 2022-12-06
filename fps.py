import time
from math import nan

class FPSCounter:
    def __init__(self, message, period=1.) -> None:
        self.fps = nan
        self.message = message
        self.period = period
        self.reset()
    
    def reset(self):
        self.cnt = 0
        self.stime = time.time()
    
    def count(self):
        self.cnt += 1
        time_slapse = time.time() - self.stime
        if time_slapse > self.period:
            self.fps = self.cnt / time_slapse
            print(self.message, ': ', self.fps, ' fps', sep='')
            self.cnt = 0
            self.stime = time.time()


