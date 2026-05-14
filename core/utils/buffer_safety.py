class SafeBuffer:
    def __init__(self, max_size_mb=50):
        self.max_bytes = max_size_mb * 1024 * 1024
        self.current_size = 0

    def can_add(self, data_len):
        return (self.current_size + data_len) <= self.max_bytes
