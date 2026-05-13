import collections

class JitterBuffer:
    def __init__(self, size=5):
        self.buffer = collections.deque(maxlen=size)
    
    def push(self, packet):
        self.buffer.append(packet)
