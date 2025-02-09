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

def update_asset(asset_data: CapCoinAsset):
    try:
        with db.atomic():
            asset = Assets.get_or_none(Assets.id == asset_data.id)
            if asset is None:
                raise HTTPException(status_code=404, detail="Actif introuvable, impossible de mettre à jour.")

            asset.rank = asset_data.rank
            asset.symbol = asset_data.symbol
            asset.name = asset_data.name
            asset.supply = asset_data.supply
            asset.maxSupply = asset_data.maxSupply
            asset.marketCapUsd = asset_data.marketCapUsd
            asset.volumeUsd24Hr = asset_data.volumeUsd24Hr
            asset.priceUsd = asset_data.priceUsd
            asset.changePercent24Hr = asset_data.changePercent24Hr
            asset.vwap24Hr = asset_data.vwap24Hr
            asset.explorer = asset_data.explorer

            asset.save()
        return asset
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la mise à jour de l'actif : {e}")


def get_asset_by_id(asset_id: str):
    try:
        asset = Assets.get_or_none(Assets.id == asset_id)
        if asset is None:
            raise HTTPException(status_code=404, detail="Actif introuvable.")
        return asset
    except Exception as e:
        print(f'{e}')
