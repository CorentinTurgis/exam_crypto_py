from fastapi import APIRouter

from app.core.requests import LoginRequest, RegisterRequest
from app.core.responses.auth_router_responses import RegisterResponse, LoginResponse
from app.services import get_user_by, save_user

auth_router = APIRouter()

@auth_router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest) -> LoginResponse:
    try:
        user = get_user_by('email', req.email)
        return LoginResponse(token=user.username+'_secret')
    except Exception as e:
        print(f'ERREUR : {e}')
    return LoginResponse(token='')


@auth_router.post("/register", response_model=RegisterResponse)
def register(req: RegisterRequest) -> RegisterResponse:
    try:
        if get_user_by('email', req.email) is not None:
            return RegisterResponse(token='', detail='User already exist')
        save_user(req)
        return RegisterResponse(token=f'{req.username}_secret', detail='')
    except Exception as e:
        print(f'ERREUR : {e}')
    return RegisterResponse(token='', detail='')
