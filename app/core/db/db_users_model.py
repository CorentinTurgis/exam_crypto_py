from datetime import datetime, timezone

from peewee import AutoField, CharField, DateTimeField

from .db_base_model import BaseModel

class DbUsersModel(BaseModel):
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
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    # Met à jour automatiquement le champ "updated_at" à chaque sauvegarde
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)