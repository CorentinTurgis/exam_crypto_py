import requests

from app.models import CapCoinAsset
from app.services import add_asset


class CoinCap:
    BASE_URL = "https://api.coincap.io/v2/assets"

    @classmethod
    def fetch_and_store_asset(cls, asset_id: str):
        url = f"{cls.BASE_URL}/{asset_id}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération de l'actif: {response.status_code}")

        data = response.json()['data']
        if not data:
            raise Exception("Données d'actif non trouvées")

        print(data)

        asset = CapCoinAsset(
            id=data["id"],
            rank=int(data["rank"]),
            symbol=data["symbol"],
            name=data["name"],
            supply=float(data["supply"]),
            maxSupply=float(data.get("maxSupply", 0)),
            marketCapUsd=float(data["marketCapUsd"]),
            volumeUsd24Hr=float(data["volumeUsd24Hr"]),
            priceUsd=float(data["priceUsd"]),
            changePercent24Hr=float(data["changePercent24Hr"]),
            vwap24Hr=float(data["vwap24Hr"]),
            explorer=data['explorer'],
        )

        print(asset)

        return add_asset(asset)