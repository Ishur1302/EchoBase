import json
import time

def log_event(event_type, message):
    log_entry = {
        "timestamp": time.time(),
        "type": event_type,
        "message": message
    }
    print(json.dumps(log_entry))
