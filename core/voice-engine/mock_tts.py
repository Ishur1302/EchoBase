import time

def mock_synthesize(text):
    print(f"TTS: Synthesizing -> {text}")
    # Simulate processing delay based on text length
    time.sleep(len(text) * 0.05)
    return b'\x00' * 1024  # Returns dummy silent PCM data
