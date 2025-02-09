from app.core.db import BaseModel, Wallets, Assets
from peewee import ForeignKeyField, AutoField, FloatField


class Cryptos(BaseModel):
    """
    Modèle représentant un portefeuille crypto.
    """
    id = AutoField(unique=True)
    asset_id = ForeignKeyField(Assets, backref="cryptos", to_field="id")
    wallet_id = ForeignKeyField(Wallets, backref="wallets", to_field="id")
    qtt = FloatField()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
