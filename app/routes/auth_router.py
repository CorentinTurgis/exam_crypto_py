from fastapi import APIRouter

from app.core.db import Users
from app.core.requests import LoginRequest, RegisterRequest
from app.core.responses import LoginResponse, RegisterResponse
from app.services import get_user_by, encode_token, save_user

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
        user: Users = get_user_by('email', req.email)
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


@auth_router.get("/test")
def list_users(current_user=Depends(get_current_user)):
    return current_user

''' 

@app.get("/cardgame/{number_of_player}")
def distribute_game(number_of_player: int)

/wallets/create  &&  /wallets/{id}/add &&  /wallets/{id}/recap  && /wallets/{id}/detail

wallet_service
create_wallet()
update_wallet_name()
add_crypto()
get_wallet_recap()
get_wallet_detail() 
''' 

