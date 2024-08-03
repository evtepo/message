from abc import abstractmethod, ABC
from datetime import datetime, UTC
from typing import TypeVar

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from config.settings import settings
from schemas.message import CreateMessage


Model = TypeVar("Model", CreateMessage, ...)


class BaseRepository(ABC):
    @abstractmethod
    async def get(self, collection_name: str, offset: int, limit: int):
        raise NotImplementedError

    @abstractmethod
    async def create(self, collection_name: str, data: Model):
        raise NotImplementedError

    @abstractmethod
    async def close(self):
        raise NotImplementedError


class MongoRepository(BaseRepository):
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(
            f"mongodb://{settings.mongo_user}:{settings.mongo_password}@{settings.mongo_host}:{settings.mongo_port}/"
        )
        self.database: AsyncIOMotorDatabase = self.client[settings.mongo_db_name]

    async def get(self, collection_name: str, offset: int, limit: int):
        collection: AsyncIOMotorCollection = self.database[collection_name]
        offset = (offset - 1) * limit
        try:
            messages = await collection.find().skip(offset).limit(limit).to_list(None)
            return messages
        except Exception:
            return []

    async def create(self, collection_name: str, data: Model) -> str:
        collection: AsyncIOMotorCollection = self.database[collection_name]
        try:
            data = data.model_dump()
            data["time"] = datetime.now(UTC)

            result = await collection.insert_one(data)
            return str(result.inserted_id)
        except Exception:
            return ""

    async def close(self):
        await self.client.close()


db: None | BaseRepository = None


async def get_storage():
    global db
    if not db:
        db = MongoRepository()

    return db
