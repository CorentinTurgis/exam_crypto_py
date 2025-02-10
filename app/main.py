import contextlib

from fastapi import FastAPI

from app.core.db import db, Users, Assets, Wallets, Cryptos
from app.routes import auth_router, wallet_router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([Users, Assets, Cryptos, Wallets])

    yield

    if not db.is_closed():
        db.close()


def create_application() -> FastAPI:
    app = FastAPI(title="crypto_api", version="1.0.0", lifespan=lifespan)

    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(wallet_router, prefix="/wallet", tags=["wallet"])
    db.connect()
    return app


app = create_application()
