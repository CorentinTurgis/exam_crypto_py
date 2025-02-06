from fastapi import APIRouter, HTTPException

from app.core.db import User, db
from app.core.requests import LoginRequest, RegisterRequest
from app.core.responses.auth_router_responses import RegisterResponse, LoginResponse

auth_router = APIRouter()

@auth_router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest) -> LoginResponse:
    try:
        user: User = User.get_or_none(User.email == req.email)
        if user is None:
            raise HTTPException(status_code=404, detail="user_not_found")
        return LoginResponse(token=user.username+'_secret')
    except Exception as e:
        print(f'ERREUR : {e}')
    return LoginResponse(token='')


@auth_router.post("/register", response_model=RegisterResponse)
def register(req: RegisterRequest) -> RegisterResponse:
    print(req)
    try:
        old_user: User = User.get_or_none(User.email == req.email)
        if old_user is not None:
            raise HTTPException(status_code=422, detail="Unprocessable Entity")
        with db.atomic():
            User.create(
                first_name=req.first_name,
                last_name=req.last_name,
                username=req.username,
                email=req.email,
                password=req.password
            )
        return RegisterResponse(token=f'{req.username}_secret')
    except Exception as e:
        print(f'ERREUR : {e}')
    return RegisterResponse(token='')
