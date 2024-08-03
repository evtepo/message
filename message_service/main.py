from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.v1.message import router as message_router
from config.settings import settings
from db.repository import db, MongoRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    global db
    db = MongoRepository()

    yield

    await db.close()


app = FastAPI(
    title=settings.title,
    lifespan=lifespan,
)

app.include_router(message_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.localhost,
        port=settings.localport,
    )
