class TurnManager:
    def __init__(self, base_timeout=0.8):
        self.timeout = base_timeout

    def adjust_for_noise(self, db_level):
        # If it's noisy, increase the timeout so we don't cut the user off
        if db_level > -30: 
            self.timeout = 1.5
        else:
            self.timeout = 0.8
