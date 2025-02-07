from app.core.db import Users
from app.services import get_user_by



def encode_token(username: str) -> str:
    """
    Encode le token
    """
    return f"{username}_secret"

def decode_token(token: str) -> Users or None:
    """
    Décode un token et retourne l'utilisateur correspondant.
    """
    try:
        username = token.split('_')[0]
        return get_user_by('username', username)
    except Exception as e:
        print(f'ERREUR : {e}')
        return None
