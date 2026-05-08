import re

def get_sentences(text_stream):
    """Yields complete sentences from a running text stream."""
    buffer = ""
    for chunk in text_stream:
        buffer += chunk
        # Split on punctuation followed by space or newline
        parts = re.split(r'([.!?])\s+', buffer)
        while len(parts) > 2:
            yield parts[0] + parts[1]
            parts = parts[2:]
        buffer = parts[0]
