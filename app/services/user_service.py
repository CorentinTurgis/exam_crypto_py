from fastapi import HTTPException

from app.core.db import Users, db
from app.core.requests import RegisterRequest

def get_user_by_id(user_id) -> Users or None:
    try:
        user = Users.get_or_none(Users.id == user_id)
        if user is None:
            raise HTTPException(status_code=404, detail='user_not_found')
        return user
    except Exception as e:
        print(f'ERREUR : {e}')
    return None

def get_user_by(field: str, value: str) -> Users or None:
    try:
        user: Users or None = Users.get_or_none(getattr(Users, field) == value)
        return user
    except Exception as e:
        print(f"ERREUR e: {e}")
    return None

def save_user(user_req: RegisterRequest) -> None:
    with db.atomic():
        Users.create(
            first_name=user_req.first_name,
            last_name=user_req.last_name,
            username=user_req.username,
            email=user_req.email,
            password=user_req.password
        )

class UsersService(Users):
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, password: str):
        self.id = user_id
        self.firstName = first_name
        self.Lastname = last_name
        self.email = email
        self.password = password

    def update_email(self, new_email: str):
        self.email = new_email

    def update_password(self, new_password: str):
        self.password = new_password

    def set_firstName(self, firstName: str):
        self.firstName = firstName
    
    def set_lastName(self, lastName: str):
        self.lastName = lastName

    def get_full_name(self) -> str:
        return f"{self.firstName} {self.Lastname}"



# Exemple :
'''
if __name__ == "__main__":
    user_service = UserService(user_id=1, first_name="John", last_name="Doe", email="john.doe@example.com", password="securepassword123")
'''