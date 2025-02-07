from fastapi import APIRouter

from app.core.db import User
from app.core.requests import LoginRequest, RegisterRequest
from app.core.responses.auth_router_responses import RegisterResponse, LoginResponse
from app.services import get_user_by, save_user, encode_token

auth_router = APIRouter()

from fastapi import APIRouter, Depends
from app.core.dependencies.auth_dependency import get_current_user

user_router = APIRouter()

@auth_router.get("/test")
def list_users(current_user=Depends(get_current_user)):
    return current_user


@auth_router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest) -> LoginResponse:
    try:
        user: User = get_user_by('email', req.email)
        if user is not None:
            return LoginResponse(token=encode_token(user.username))
    except Exception as e:
        print(f'ERREUR : {e}')
    return LoginResponse(token='')


@auth_router.post("/register", response_model=RegisterResponse)
def register(req: RegisterRequest) -> RegisterResponse:
    try:
        if get_user_by('email', req.email) is not None:
            return RegisterResponse(token='', detail='User already exist')
        save_user(req)
        return RegisterResponse(token=encode_token(req.username), detail='Ok')
    except Exception as e:
        print(f'ERREUR : {e}')
    return RegisterResponse(token='', detail='Unexpected exception')
