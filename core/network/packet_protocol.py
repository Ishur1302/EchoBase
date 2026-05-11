import struct

def wrap_packet(sequence_id, audio_data):
    # Pack sequence ID as 4-byte unsigned int followed by raw bytes
    header = struct.pack('!I', sequence_id)
    return header + audio_data
