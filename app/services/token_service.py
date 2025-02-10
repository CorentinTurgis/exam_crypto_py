import datetime
import os

import jwt
import pytz
from dotenv import load_dotenv

from app.core.db import Users
from app.services import get_user_by

TZ = pytz.timezone("Europe/Paris")

load_dotenv()

SECRET = os.getenv('SECRET_KEY')

def encode_token(username: str) -> str:
    """
    Génère un token JWT contenant l'username et une expiration.
    """
    now = datetime.datetime.now(datetime.UTC)
    payload = {
        "exp": now + datetime.timedelta(hours=1),
        "iat": now,
        "sub": username
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def decode_token(token: str) -> Users or None:
    """
    Décode un token JWT et retourne l'utilisateur correspondant.
    """
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        username = payload.get("sub")
        return get_user_by('username', username)
    except jwt.ExpiredSignatureError:
        print("ERREUR : Token expiré")
    except jwt.InvalidTokenError:
        print("ERREUR : Token invalide")
    except Exception as e:
        print(f'ERREUR : {e}')
    return None