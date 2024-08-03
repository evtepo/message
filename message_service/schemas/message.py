from datetime import datetime

from pydantic import BaseModel


class BaseMessage(BaseModel):
    author: str
    text: str


class Message(BaseMessage):
    time: datetime

    class Config:
        from_attributes = True


class CreateMessage(BaseMessage): ...
