from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.db.db_cryptos_model import Cryptos
from app.core.dependencies.auth_dependency import get_current_user
from app.core.responses import CreateWalletResponse, AddToWalletResponse, RecapResponse, DetailResponse
from app.core.requests import CreateWalletRequest, AddToWalletRequest, RecapRequest, DetailRequest

from app.core.db import Wallets, Assets
from app.core.responses.wallet_router_responses import AssetDetail
from app.services import get_asset_by_id, CoinCap
from app.services.crypto_service import get_crypto_by_wallet_and_asset, update_crypto_qtt, save_crypto
from app.services.wallet_service import save_wallet, get_wallet_by_user_id

wallet_router = APIRouter()

@wallet_router.post("/create", response_model=CreateWalletResponse)
def create_wallet(req: CreateWalletRequest, current_user=Depends(get_current_user)) -> CreateWalletResponse:
    save_wallet(req.name, current_user.id)
    return CreateWalletResponse(detail='Super')
    # try:
    #     token = get_user_by('token', req.token) # Vérifie si l'utilisateur existe
    #     if token is not None:
    #         return CreateResponse(detail="Portefeuile créé avec succès")
    # except Exception as e:
    #     print(f'ERREUR : {e}')
    #     return CreateResponse(detail="Erreur lors de la création")

@wallet_router.post("/add", response_model=AddToWalletResponse)
def add_to_wallet(req: AddToWalletRequest, current_user=Depends(get_current_user)) -> AddToWalletResponse:
    try:
        user_id = current_user.id
        wallet: Wallets = get_wallet_by_user_id(user_id)
        asset: Assets = CoinCap.fetch_and_store_asset(req.crypto_id)
        qtt = req.amount
        crypto: Cryptos = get_crypto_by_wallet_and_asset(wallet=wallet, asset=asset)
        if crypto:
            update_crypto_qtt(crypto=crypto, qtt=qtt)
            return AddToWalletResponse(detail=f'Nouveau montant : {crypto.qtt}')
        else:
            save_crypto(wallet=wallet, asset=asset, qtt=qtt)
            return AddToWalletResponse(detail=f'Nouvelle crypto : {crypto.id} * {crypto.qtt}')
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
    crypto_list = []
    for c in query:
        print(c)
    print(crypto_list)
    return DetailResponse(crypto_list=crypto_list, detail="Ca fonctionne")
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

