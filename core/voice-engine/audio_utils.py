import numpy as np

def normalize_audio(audio_bytes):
    # Convert bytes to numpy array
    audio_data = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32)
    # Normalize to -1.0 to 1.0 range
    max_val = np.max(np.abs(audio_data))
    if max_val > 0:
        audio_data /= max_val
    return audio_data
