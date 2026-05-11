class SessionPool:
    def __init__(self):
        self.active_sessions = {}

    def register(self, session_id, socket):
        self.active_sessions[session_id] = socket

    def unregister(self, session_id):
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
