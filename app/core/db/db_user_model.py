from datetime import datetime

from peewee import AutoField, CharField, DateTimeField

from . import PARIS_TIMEZONE
from .db_base_model import BaseModel

class User(BaseModel):
    """
    Modèle utilisateur Peewee.
      - email : email unique
      - password : mot de passe
      - created_at : date de création
      - updated_at : date de dernière mise à jour
    """
    id = AutoField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField(default=lambda: datetime.now(PARIS_TIMEZONE))
    updated_at = DateTimeField(default=lambda: datetime.now(PARIS_TIMEZONE))

    # Met à jour automatiquement le champ "updated_at" à chaque sauvegarde
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(PARIS_TIMEZONE)
        return super().save(*args, **kwargs)