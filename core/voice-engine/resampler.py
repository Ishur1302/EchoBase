import numpy as np

def resample_audio(audio_data, original_rate, target_rate):
    # Simple linear interpolation for resampling
    duration = len(audio_data) / original_rate
    num_target_samples = int(duration * target_rate)
    return np.interp(
        np.linspace(0, duration, num_target_samples),
        np.linspace(0, duration, len(audio_data)),
        audio_data
    )
