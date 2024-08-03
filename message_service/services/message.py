from db.repository import BaseRepository
from schemas.message import CreateMessage


async def list_of_messages(collection: str, page: int, size: int, db: BaseRepository):
    messages = await db.get(collection, page, size)

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if messages and len(messages) == size else None

    return {
        "links": {
            "prev": prev_page,
            "next": next_page,
        },
        "data": messages,
    }


async def create_single_message(message: CreateMessage, collection: str, db: BaseRepository):
    new_message = await db.create(collection, message)

    return {"id": new_message}
