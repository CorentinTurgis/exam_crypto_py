from app.core.db import BaseModel, Users
from peewee import ForeignKeyField, CharField, AutoField


class Wallets(BaseModel):
    """
    Modèle représentant un portefeuille crypto.
    """
    id = AutoField(unique=True)
    name = CharField()
    owner = ForeignKeyField(Users, backref="wallets", to_field="id", unique=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
