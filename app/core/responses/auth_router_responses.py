from pydantic import BaseModel


class RegisterResponse(BaseModel):
    token: str
    detail: str or None

class LoginResponse(BaseModel):
    token: str