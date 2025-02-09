from typing import Any

from fastapi import APIRouter, Depends

from app.core.db.db_cryptos_model import Cryptos
from app.core.dependencies.auth_dependency import get_current_user
from app.core.responses import CreateWalletResponse, AddToWalletResponse, DetailResponse
from app.core.requests import CreateWalletRequest, AddToWalletRequest

from app.core.db import Wallets, Assets, Users
from app.core.responses.wallet_router_responses import AssetDetail
from app.services import CoinCap
from app.services.crypto_service import get_crypto_by_wallet_and_asset, update_crypto_qtt, save_crypto
from app.services.wallet_service import save_wallet, get_wallet_by_user_id

wallet_router = APIRouter()

@wallet_router.post("/create", response_model=CreateWalletResponse)
def create_wallet(req: CreateWalletRequest, current_user=Depends(get_current_user)) -> CreateWalletResponse:
    save_wallet(req.name, current_user.id)
    return CreateWalletResponse(detail='Super')

@wallet_router.post("/add", response_model=Any)
def add_to_wallet(req: AddToWalletRequest, current_user:Users=Depends(get_current_user)) -> Any:
    try:
        user_id: int = current_user.id
        wallet: Wallets = get_wallet_by_user_id(user_id)
        asset: Assets = CoinCap.fetch_and_store_asset(req.crypto_id)
        qtt = req.amount
        crypto: Cryptos = get_crypto_by_wallet_and_asset(wallet=wallet, asset=asset)
        if crypto:
            update_crypto_qtt(crypto=crypto, qtt=qtt)
            return AddToWalletResponse(detail=f'Nouveau montant : {crypto.qtt}')
        else:
            save_crypto(wallet=wallet, asset=asset, qtt=qtt)
            return AddToWalletResponse(detail=f'Nouvelle crypto : {asset.id} * {qtt}')
    except Exception as e:
        print(f"ERREUR : {e}")
        return AddToWalletResponse(detail='Erreur lors de l\'ajout de la crypto')
    # try:
    #     if id is not None:
    #         return AddToWalletResponse(detail="Cryptomonnaie ajoutée avec succès")
    # except Exception as e:
    #     print(f'ERREUR : {e}')
    #     return AddToWalletResponse(detail="Erreur lors de l'ajout de la cryptomonnaie")
#
#
# @auth_router.post("/wallets/{id}/recap", response_model=RecapResponse)
# def RecapWallet(id: str, req: RecapRequest) -> RecapResponse:
#     try:
#         if id is not None:
#             return RecapResponse(detail="Cryptomonnaie ajoutée avec succès")
#     except Exception as e:
#         print(f'ERREUR : {e}')
#         return RecapResponse(detail="Erreur lors de la récuparation du portefeuille")

@wallet_router.get("/detail", response_model=DetailResponse)
def get_wallet_detail(current_user=Depends(get_current_user)):
    query = (Cryptos
             .select(Cryptos, Wallets, Assets)
             .join(Wallets)
             .switch(Cryptos)
             .join(Assets)
             .where(Wallets.owner == current_user.id)
             )
    asset_detail_list = []
    asset_ids = [str(asset.asset_id.id) for asset in query]
    assets_str = ','.join(asset_ids)
    CoinCap.fetch_and_store_asset_list(assets_str)
    for c in query:
        asset_detail = AssetDetail(
            asset_name=c.asset_id.id,
            qtt=c.qtt,
            total_price=c.qtt * c.asset_id.priceUsd
        )
        asset_detail_list.append(asset_detail)
    wallet_price = sum(elem.total_price for elem in asset_detail_list)
    return DetailResponse(crypto_list=asset_detail_list, detail="Ca fonctionne", wallet_price=wallet_price)
    # try:
    #     if id is not None:
    #         return DetailResponse(detail="Cryptomonnaie ajoutée avec succès")
    # except Exception as e:
    #     print(f'ERREUR : {e}')
    #     return DetailResponse(detail="Erreur lors de la récuparation de la liste de vos cryptomonnaies")


''' 
wallet_service
create_wallet()
update_wallet_name()
add_crypto()
get_wallet_recap()
get_wallet_detail() 
''' 

