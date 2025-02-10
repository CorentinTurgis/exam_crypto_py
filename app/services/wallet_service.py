from fastapi import HTTPException

from app.core.db import db, Wallets


def save_wallet(name: str, owner: str) -> None:
    with db.atomic():
        Wallets.create(
            name=name,
            owner=owner
        )

def get_wallet_by_user_id(user_id) -> Wallets or None:
    try:
        wallet = Wallets.get_or_none(Wallets.owner == user_id)
        if wallet is None:
            raise HTTPException(status_code=404, detail='wallet_not_found')
        return wallet
    except Exception as e:
        print(f'ERREUR : {e}')
    return None