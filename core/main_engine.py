class EchoBaseEngine:
    def __init__(self):
        self.is_active = True
    
    def process_voice_input(self, audio_stream):
        print("Processing audio...")
        # Placeholder for VAD -> LLM logic
