from fastapi import HTTPException

from app.core.db import Assets, db
from app.models import CapCoinAsset


def add_asset(asset_data: CapCoinAsset):
    """
    Ajoute un actif crypto en base de données.
    """
    try:
        with db.atomic():
            asset = Assets.create(
                id=asset_data.id,
                rank=asset_data.rank,
                symbol=asset_data.symbol,
                name=asset_data.name,
                supply=asset_data.supply,
                maxSupply=asset_data.maxSupply,
                marketCapUsd=asset_data.marketCapUsd,
                volumeUsd24Hr=asset_data.volumeUsd24Hr,
                priceUsd=asset_data.priceUsd,
                changePercent24Hr=asset_data.changePercent24Hr,
                vwap24Hr=asset_data.vwap24Hr,
                explorer=asset_data.explorer
            )
        return asset
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de l'actif : {e}")

def get_asset_by_id(asset_id: int):
    try:
        asset = Assets.get_or_none(Assets.id == asset_id)
        if asset is None:
            raise HTTPException(status_code=404, detail="Actif introuvable.")
        return asset
    except Exception as e:
        print(f'{e}')
