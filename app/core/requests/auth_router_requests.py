from pydantic import EmailStr, BaseModel


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str