class UserService(User):
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