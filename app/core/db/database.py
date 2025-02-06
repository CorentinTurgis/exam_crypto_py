from peewee import SqliteDatabase

DATABASE_URL = "crypto_api.db"

db = SqliteDatabase(
    DATABASE_URL,
)