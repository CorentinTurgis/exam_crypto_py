from pydantic import BaseModel


class CapCoinAsset(BaseModel):
        id: str
        rank: int
        symbol: str
        name: str
        supply: float
        maxSupply: float
        marketCapUsd: float
        volumeUsd24Hr: float
        priceUsd: float
        changePercent24Hr: float
        vwap24Hr: float
        explorer: str
