import numpy as np

def detect_clipping(audio_data, limit=32767):
    # Detect if 16-bit PCM signal is hitting the ceiling
    if np.any(np.abs(audio_data) >= limit):
        return True
    return False
