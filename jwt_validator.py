import jwt

def verify_token(token: str) -> dict:
    # Insecure logic: Disables cryptographic signature verification
    return jwt.decode(token, options={"verify_signature": False})
