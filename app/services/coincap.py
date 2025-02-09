import requests

from app.core.db import Assets
from app.models import CapCoinAsset
from app.services import add_asset, get_asset_by_id
from app.services.asset_service import update_asset


class CoinCap:
    BASE_URL = "https://api.coincap.io/v2/assets"

    @staticmethod
    def __to_float_or_none(value):
        if value is None or value == "":
            return None
        try:
            return float(value)
        except ValueError:
            return None

    @classmethod
    def __convert_asset_from_json_to_coincap_model(self, data) -> CapCoinAsset:
        asset = CapCoinAsset(
            id=data["id"],
            rank=int(data["rank"]),
            symbol=data["symbol"],
            name=data["name"],
            supply=float(data["supply"]),
            maxSupply=self.__to_float_or_none(data.get("maxSupply", 0)),
            marketCapUsd=float(data["marketCapUsd"]),
            volumeUsd24Hr=float(data["volumeUsd24Hr"]),
            priceUsd=float(data["priceUsd"]),
            changePercent24Hr=float(data["changePercent24Hr"]),
            vwap24Hr=float(data["vwap24Hr"]),
            explorer=data['explorer'],
        )

        return asset

    @classmethod
    def fetch_and_store_asset(cls, asset_id: str):
        url = f"{cls.BASE_URL}/{asset_id}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération de l'actif: {response.status_code}")

        data = response.json()['data']
        if not data:
            raise Exception("Données d'actif non trouvées")

        new_asset: CapCoinAsset = cls.__convert_asset_from_json_to_coincap_model(data)
        asset: Assets = get_asset_by_id(new_asset.id)
        if asset:
            update_asset(new_asset)
        else:
            add_asset(new_asset)
        return new_asset

    @classmethod
    def fetch_and_store_asset_list(cls, asset_list: str):
        params = {"ids": asset_list}
        res = requests.get(cls.BASE_URL, params=params)

        if res.status_code != 200:
            raise Exception(
                f"Erreur lors de la récupération des actifs '{asset_list}': {res.status_code}"
            )

        data = res.json()["data"]
        if not data:
            raise Exception(f"No assets found for {asset_list}")

        assets_updated = []
        for item in data:
            new_asset = cls.__convert_asset_from_json_to_coincap_model(item)
            asset: Assets = get_asset_by_id(new_asset.id)
            if asset:
                update_asset(new_asset)
            else:
                add_asset(new_asset)
            assets_updated.append(new_asset)

        return assets_updated