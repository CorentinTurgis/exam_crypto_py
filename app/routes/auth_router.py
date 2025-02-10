from fastapi import APIRouter, HTTPException

from app import services
from app.core import (
    db,
    requests as my_requests,
    responses as my_responses,
)


auth_router = APIRouter()


@auth_router.post("/login", response_model=my_responses.LoginResponse)
def login(req: my_requests.LoginRequest) -> my_responses.LoginResponse:
    try:
        user: db.Users = services.get_user_by('email', req.email)
        if user is not None:
            return my_responses.LoginResponse(token=services.encode_token(user.username), detail='Connecté, ajoutez le token dans Authorization')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Imposssible de se connecter')
    raise HTTPException(status_code=401, detail=f'login/email invalides')


@auth_router.post("/register", response_model=my_responses.RegisterResponse)
def register(req: my_requests.RegisterRequest) -> my_responses.RegisterResponse:
    try:
        if services.get_user_by('email', req.email) is not None:
            raise HTTPException(status_code=422, detail=f'Un compte existe pour l\'email {req.email}')
        services.save_user(req)
        return my_responses.RegisterResponse(token=services.encode_token(req.username), detail='Connecté, ajoutez le token dans Authorization')
    except Exception:
        raise HTTPException(status_code=500, detail=f'Imposssible de se connecter')
