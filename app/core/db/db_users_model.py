from peewee import AutoField, CharField

from .db_base_model import BaseModel

class Users(BaseModel):
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

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
