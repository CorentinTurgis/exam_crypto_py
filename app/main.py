import contextlib

from fastapi import FastAPI

from app.api.routes import auth_router
from app.core.db import db, Users


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([Users])

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