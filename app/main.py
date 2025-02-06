import contextlib

from fastapi import FastAPI

from app.core.db import db, DbUsersModel


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([DbUsersModel])

    yield

    if not db.is_closed():
        db.close()


def create_application() -> FastAPI:
    app = FastAPI(title="crypto_api", version="1.0.0", lifespan=lifespan)
    # On inclut les routers
    # app.include_router(users_router, prefix="/users", tags=["users"])
    db.connect()
    return app

app = create_application()