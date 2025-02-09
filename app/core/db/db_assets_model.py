from peewee import CharField, FloatField, IntegerField

from app.core.db import BaseModel


class Assets(BaseModel):
    id = CharField()
    rank = IntegerField()
    symbol = CharField()
    name = CharField()
    supply = FloatField()
    maxSupply = FloatField(null=True)
    marketCapUsd = FloatField()
    volumeUsd24Hr = FloatField()
    priceUsd = FloatField()
    changePercent24Hr = FloatField()
    vwap24Hr = FloatField()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)