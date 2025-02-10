from fastapi import APIRouter, Depends

from app.core import (
    db,
    dependencies,
    requests as my_requests,
    responses as my_responses,
)

from app import services
from app.services import CoinCap

wallet_router = APIRouter()

@wallet_router.post("/create", response_model=my_responses.CreateWalletResponse)
def create_wallet(req: my_requests.CreateWalletRequest, current_user=Depends(dependencies.get_current_user)) -> my_responses.CreateWalletResponse:
    services.save_wallet(req.name, current_user.id)
    return my_responses.CreateWalletResponse(detail='Super')

@wallet_router.post("/add", response_model=my_responses.AddToWalletResponse)
def add_to_wallet(req: my_requests.AddToWalletRequest, current_user:db.Users=Depends(dependencies.get_current_user)) -> my_responses.AddToWalletResponse:
    try:
        user_id: int = current_user.id
        wallet: db.Wallets = services.get_wallet_by_user_id(user_id)
        asset: db.Assets = CoinCap.fetch_and_store_asset(req.crypto_id)
        qtt = req.amount
        crypto: db.Cryptos = services.get_crypto_by_wallet_and_asset(wallet=wallet, asset=asset)
        if crypto:
            services.update_crypto_qtt(crypto=crypto, qtt=qtt)
            return my_responses.AddToWalletResponse(detail=f'Nouveau montant : {crypto.qtt}')
        else:
            services.save_crypto(wallet=wallet, asset=asset, qtt=qtt)
            return my_responses.AddToWalletResponse(detail=f'Nouvelle crypto : {asset.id} * {qtt}')
    except Exception as e:
        print(f"ERREUR : {e}")
        return my_responses.AddToWalletResponse(detail='Erreur lors de l\'ajout de la crypto')

@wallet_router.get("/detail", response_model=my_responses.DetailResponse)
def get_wallet_detail(current_user=Depends(dependencies.get_current_user)) -> my_responses.DetailResponse:
    query = (db.Cryptos
             .select(db.Cryptos, db.Wallets, db.Assets)
             .join(db.Wallets)
             .switch(db.Cryptos)
             .join(db.Assets)
             .where(db.Wallets.owner == current_user.id)
             )
    asset_detail_list = []
    asset_ids = [str(asset.asset_id.id) for asset in query]
    assets_str = ','.join(asset_ids)
    CoinCap.fetch_and_store_asset_list(assets_str)
    for c in query:
        asset_detail = my_responses.AssetDetail(
            asset_name=c.asset_id.id,
            qtt=c.qtt,
            total_price=c.qtt * c.asset_id.priceUsd
        )
        asset_detail_list.append(asset_detail)
    wallet_price = sum(elem.total_price for elem in asset_detail_list)
    return my_responses.DetailResponse(crypto_list=asset_detail_list, detail="Ca fonctionne", wallet_price=wallet_price)

