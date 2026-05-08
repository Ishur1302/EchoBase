import heapq

class SpeechQueue:
    def __init__(self):
        self.queue = []

    def add_phrase(self, phrase, priority=1):
        # Higher priority (lower number) moves to the front
        heapq.heappush(self.queue, (priority, phrase))

    def get_next(self):
        return heapq.heappop(self.queue)[1] if self.queue else None
