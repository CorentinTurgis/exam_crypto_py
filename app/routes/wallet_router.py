from fastapi import APIRouter
from app.core.responses import CreateResponse, AddResponse, RecapResponse, DetailResponse
from app.core.requests import CreateRequest, AddRequest, RecapRequest, DetailRequest

from app.core.db import Wallets

auth_router = APIRouter()

@auth_router.post("/wallets/create", response_model=CreateResponse)
def CreateWallet(req: CreateRequest) -> CreateResponse:
    try:
        token = get_user_by('token', req.token) # Vérifie si l'utilisateur existe
        if token is not None:
            return CreateResponse(detail="Portefeuile créé avec succès")
    except Exception as e:
        print(f'ERREUR : {e}')
        return CreateResponse(detail="Erreur lors de la création")

@auth_router.post("/wallets/{id}/add", response_model=AddResponse)
def AddToWallet(id: str, req: AddRequest) -> AddResponse:
    try:
        if id is not None:
            return AddResponse(detail="Cryptomonnaie ajoutée avec succès")
    except Exception as e:
        print(f'ERREUR : {e}')
        return AddResponse(detail="Erreur lors de l'ajout de la cryptomonnaie")


@auth_router.post("/wallets/{id}/recap", response_model=RecapResponse)
def RecapWallet(id: str, req: RecapRequest) -> RecapResponse:
    try:
        if id is not None:
            return RecapResponse(detail="Cryptomonnaie ajoutée avec succès")
    except Exception as e:
        print(f'ERREUR : {e}')
        return RecapResponse(detail="Erreur lors de la récuparation du portefeuille")

@auth_router.post("//wallets/{id}/detail", response_model=DetailResponse)
def DetailWallet(id: str, req: DetailRequest) -> DetailResponse:
    try:
        if id is not None:
            return DetailResponse(detail="Cryptomonnaie ajoutée avec succès")
    except Exception as e:
        print(f'ERREUR : {e}')
        return DetailResponse(detail="Erreur lors de la récuparation de la liste de vos cryptomonnaies")


''' 
wallet_service
create_wallet()
update_wallet_name()
add_crypto()
get_wallet_recap()
get_wallet_detail() 
''' 

