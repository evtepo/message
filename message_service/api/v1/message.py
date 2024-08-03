from typing import Annotated

from fastapi import APIRouter, status, Depends, Query

from db.repository import BaseRepository, get_storage
from models.collection import Collection
from schemas.message import CreateMessage, Message
from services.message import create_single_message, list_of_messages


router = APIRouter(prefix="/api/v1", tags=["Message"])

db_dependency = Annotated[BaseRepository, Depends(get_storage)]


@router.get(
    "/messages/",
    response_model=dict[str, dict | list[Message | None]],
    status_code=status.HTTP_200_OK,
)
async def get_messages(
    db: db_dependency,
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=10, le=50, default=10),
):
    return await list_of_messages(Collection.message.value, page, size, db)


@router.post("/messages/", response_model=Message | dict, status_code=status.HTTP_201_CREATED)
async def create_message(message: CreateMessage, db: db_dependency):
    return await create_single_message(message, Collection.message.value, db)
