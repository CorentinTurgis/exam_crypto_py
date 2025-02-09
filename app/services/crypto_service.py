from app.core.db import db, Wallets, Assets
from app.core.db.db_cryptos_model import Cryptos


def get_crypto_by_wallet_and_asset(wallet: Wallets, asset: Assets):
    crypto: Cryptos = Cryptos.get_or_none(
        (Cryptos.wallet_id == wallet.id) and (Cryptos.wallet_id == asset.id)
    )
    return crypto

def save_crypto(wallet: Wallets, asset: Assets, qtt: float) -> None:
    with db.atomic():
        Cryptos.create(
            wallet_id=wallet.id,
            asset_id=asset.id,
            qtt=qtt
        )

def update_crypto_qtt(crypto: Cryptos, qtt: float):
    if crypto:
        crypto.qtt += qtt
        crypto.save()
        return crypto