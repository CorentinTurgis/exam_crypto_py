from fastapi import HTTPException

from app.core import db


def save_wallet(name: str, owner: str) -> None:
    try:
        with db.db.atomic():
            db.Wallets.create(
                name=name,
                owner=owner
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail='Impossible de créer le wallet')

def get_wallet_by_user_id(user_id) -> db.Wallets:
    try:
        wallet: db.Wallets = db.Wallets.get_or_none(db.Wallets.owner == user_id)
        if wallet is None:
            raise HTTPException(status_code=404, detail='wallet_not_found')
        return wallet
    except Exception as e:
        raise HTTPException(status_code=500, detail='Impossible de recuperer le wallet')