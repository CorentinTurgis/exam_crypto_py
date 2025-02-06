from fastapi import APIRouter, HTTPException

from app.core.db import User, db
from app.core.requests import LoginRequest, RegisterRequest
from app.core.responses.auth_router_responses import RegisterResponse, LoginResponse

auth_router = APIRouter()


@auth_router.post("/login", response_model=LoginResponse)
def login(user_data: LoginRequest) -> LoginResponse:
    try:
        user: User = User.get_or_none(User.email == user_data.email)
        if user is None:
            raise HTTPException(status_code=404, detail="user_not_found")
        return LoginResponse(token=user.username+'_secret')
    except Exception as e:
        print(f'ERREUR : {e}')
    return LoginResponse(token='')


@auth_router.post("/register", response_model=RegisterResponse)
def register(user: RegisterRequest) -> RegisterResponse:
    print(user)
    try:
        old_user: User = User.get_or_none(User.email == user.email)
        if old_user is not None:
            raise HTTPException(status_code=422, detail="Unprocessable Entity")
        with db.atomic():
            new_user = User.create(
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
                password=user.password
            )
            if user is None:
                raise HTTPException(status_code=500, detail='Server Error')
        return RegisterResponse(token=f'{user.username}_secret')
    except Exception as e:
        print(f'ERREUR : {e}')
    return RegisterResponse(token='')
