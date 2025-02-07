from app.core.db import BaseModel, Users
from peewee import AutoField, ForeignKeyField


class Wallets(BaseModel):
    """
    Modèle représentant un portefeuille crypto.
    """
    id = AutoField()
    user = ForeignKeyField(Users, backref="wallets")

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
