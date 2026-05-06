def validate_pcm_header(data):
    # Ensure chunk size is power of 2 for FFT efficiency
    return len(data) > 0 and (len(data) & (len(data) - 1)) == 0
