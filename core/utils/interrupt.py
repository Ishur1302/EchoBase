class InterruptionHandler:
    def __init__(self):
        self.is_interrupted = False

    def trigger(self):
        self.is_interrupted = True
        print("SYSTEM: User interrupted. Halting AI response.")
