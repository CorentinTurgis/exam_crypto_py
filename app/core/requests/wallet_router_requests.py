from pydantic import BaseModel

class CreateWalletRequest(BaseModel):
    name: str

class AddToWalletRequest(BaseModel):
    crypto_id: str
    amount: float

class RecapRequest(BaseModel):
    token: str

class DetailRequest(BaseModel):
    token: str