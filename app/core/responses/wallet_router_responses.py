from datetime import datetime
from pydantic import BaseModel

from app.core.db.db_cryptos_model import Cryptos


class CreateWalletResponse(BaseModel):
    detail: str

class AddToWalletResponse(BaseModel):
    detail: str

class RecapResponse(BaseModel):
    detail: str
    value: float
    numberOfAssets: int
    updateTime: datetime

class AssetDetail(BaseModel):
    asset_name: str
    qtt: float
    total_price: float

class DetailResponse(BaseModel):
    detail: str
    crypto_list: list[AssetDetail]
    wallet_price: float
