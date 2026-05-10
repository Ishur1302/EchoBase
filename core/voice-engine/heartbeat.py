import time

class AudioHeartbeat:
    def __init__(self, timeout=5.0):
        self.last_packet = time.time()
        self.timeout = timeout

    def record_packet(self):
        self.last_packet = time.time()

    def is_alive(self):
        return (time.time() - self.last_packet) < self.timeout
