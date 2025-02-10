from fastapi import APIRouter


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
            return my_responses.LoginResponse(token=services.encode_token(user.username))
    except Exception as e:
        print(f'ERREUR : {e}')
    return my_responses.LoginResponse(token='')


@auth_router.post("/register", response_model=my_responses.RegisterResponse)
def register(req: my_requests.RegisterRequest) -> my_responses.RegisterResponse:
    try:
        if services.get_user_by('email', req.email) is not None:
            return my_responses.RegisterResponse(token='', detail='User already exist')
        services.save_user(req)
        return my_responses.RegisterResponse(token=services.encode_token(req.username), detail='Ok')
    except Exception as e:
        print(f'ERREUR : {e}')
    return my_responses.RegisterResponse(token='', detail='Unexpected exception')
