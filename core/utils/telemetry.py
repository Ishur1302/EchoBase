import time

class LatencyTracker:
    def __init__(self):
        self.start_time = 0

    def start_measure(self):
        self.start_time = time.perf_counter()

    def end_measure(self, label):
        duration = (time.perf_counter() - self.start_time) * 1000
        print(f"DEBUG: {label} took {duration:.2f}ms")
