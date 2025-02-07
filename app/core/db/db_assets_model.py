from peewee import AutoField, CharField, FloatField

from app.core.db import BaseModel


class Assets(BaseModel):
    id = AutoField()
    name = CharField()
    symbol = CharField()
    price = FloatField()
    quantity = FloatField()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)