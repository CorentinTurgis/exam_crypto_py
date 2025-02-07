from app.core.db import BaseModel, User
from peewee import AutoField, ForeignKeyField


class Wallet(BaseModel):
    """
    Modèle représentant un portefeuille crypto.
    """
    id = AutoField()
    user = ForeignKeyField(User, backref="wallets")

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
