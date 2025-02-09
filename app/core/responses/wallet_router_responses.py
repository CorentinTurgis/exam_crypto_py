from datetime import datetime
from pydantic import BaseModel


class CreateResponse(BaseModel):
    detail: str

class AddResponse(BaseModel):
    detail: str

class RecapResponse(BaseModel):
    detail: str
    value: float
    numberOfAssets: int
    updateTime: datetime

class DetailResponse(BaseModel):
    detail: str
    cryptos: List[
        name: str
        quantity: float
        value: float
        updateTime: datetime
    ]

