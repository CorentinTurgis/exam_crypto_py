from fastapi import Request

from app.services import get_user_by



def encode_token(username: str) -> str:
    """
    Encode le token
    """
    return f"{username}_secret"

def decode_token(token: str):
    """
    Décode un token et retourne l'utilisateur correspondant.
    """
    try:
        username = token.split('_')[0]
        return get_user_by('username', username)
    except Exception as e:
        print(f'ERREUR : {e}')
        return None

def get_user_by_request(req: Request):
    """
    Récupère le token dans l'entête Authorization et retourne l'utilisateur correspondant.
    """
    try:
        auth_header = req.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None
        token = auth_header.split(" ")[1]  # Extraire le token après "Bearer"
        return decode_token(token)
    except Exception as e:
        print(f'ERREUR : {e}')
        return None
