from datetime import datetime

import pytz
from peewee import Model, DateTimeField

from .database import db

TZ = pytz.timezone("Europe/Paris")

class BaseModel(Model):
    class Meta:
        database = db

    created_at = DateTimeField(default=lambda: datetime.now(TZ))
    updated_at = DateTimeField(default=lambda: datetime.now(TZ))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(TZ)
        return super().save(*args, **kwargs)