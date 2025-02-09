from pydantic import BaseModel


class CreateRequest(BaseModel):
    token: str

class AddRequest(BaseModel):
    token: str
    crypto_id: str
    amount: float

class RecapRequest(BaseModel):
    token: str

class DetailRequest(BaseModel):
    token: str
    