def get_cors_config():
    return {
        "allow_origins": ["*"],  # Restrict this in production
        "allow_methods": ["POST", "GET"],
        "allow_headers": ["Authorization", "Content-Type"],
    }
