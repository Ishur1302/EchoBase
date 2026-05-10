import os

def validate_env():
    required = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "ECHO_BASE_PORT"]
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing required config: {', '.join(missing)}")
