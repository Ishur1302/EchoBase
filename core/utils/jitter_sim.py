import time
import random

def simulate_network_condition(audio_packet):
    # Simulate a 50ms-150ms delay common in mobile networks
    delay = random.uniform(0.05, 0.15)
    time.sleep(delay)
    return audio_packet
