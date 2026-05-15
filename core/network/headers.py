import struct

def create_audio_header(sample_rate=16000, channels=1):
    # Pack metadata into a 8-byte header
    return struct.pack('!II', sample_rate, channels)
