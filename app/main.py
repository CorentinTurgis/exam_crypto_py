import contextlib

from fastapi import FastAPI

from app.core.db import db, Users, Assets
from app.routes import auth_router
from app.services import CoinCap


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([Users])
    db.create_tables([Assets])

    yield

    if not db.is_closed():
        db.close()


def create_application() -> FastAPI:
    app = FastAPI(title="crypto_api", version="1.0.0", lifespan=lifespan)
    # On inclut les routers
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    db.connect()
    return app


app = create_application()
asset_to_fetch = [
     Assets(id='ethereum'),
     Assets(id='bitcoin')
 ]
CoinCap.fetch_and_store_asset_list(asset_to_fetch)
# CoinCap.fetch_and_store_asset('bitcoin')