import numpy as np

def is_silent(audio_chunk, threshold=500):
    # Calculate energy of the audio signal
    audio_data = np.frombuffer(audio_chunk, dtype=np.int16)
    rms = np.sqrt(np.mean(audio_data.astype(np.float32)**2))
    return rms < threshold
