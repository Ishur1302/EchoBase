import re

def sanitize_transcript(text):
    # Remove any non-alphanumeric characters except basic punctuation
    return re.sub(r'[^\w\s.,?!]', '', text)
