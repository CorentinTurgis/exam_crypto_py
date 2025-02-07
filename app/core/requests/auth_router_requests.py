from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str