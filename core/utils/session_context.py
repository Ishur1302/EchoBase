class SessionContext:
    def __init__(self, ttl=300):
        self.history = []
        self.expiry = ttl # 5 minute session life

    def save_context(self, message):
        self.history.append(message)
