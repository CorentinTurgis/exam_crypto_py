from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.db import Users
from app.services.token_service import decode_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Vérifie le token pour chaque requête et retourne l'utilisateur correspondant.
    """
    token = credentials.credentials
    user: Users = decode_token(token)

    if user is None:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")

    return user
