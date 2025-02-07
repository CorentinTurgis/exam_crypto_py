from datetime import datetime


from app.core.db import BaseModel, User, PARIS_TIMEZONE
from peewee import AutoField, CharField, FloatField, ForeignKeyField, DateTimeField


class Wallet(BaseModel):
    """
    Modèle représentant un portefeuille crypto.
    """
    id = AutoField()
    user = ForeignKeyField(User, backref="wallets")
    updated_at = DateTimeField(default=lambda: datetime.now(PARIS_TIMEZONE))

class CryptoAsset(BaseModel):
    """
    Modèle représentant une crypto-monnaie détenue dans un portefeuille.
    """
    id = AutoField()
    wallet = ForeignKeyField(Wallet, backref="assets", on_delete="CASCADE")
    user = ForeignKeyField(User, backref="crypto_assets", on_delete="CASCADE")
    name = CharField()
    symbol = CharField()
    price = FloatField()
    quantity = FloatField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(PARIS_TIMEZONE)
        return super().save(*args, **kwargs)