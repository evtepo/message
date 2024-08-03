from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = Field(alias="TITLE", default="Message API")
    localhost: str = Field(alias="LOCALHOST", default="localhost")
    localport: int = Field(alias="LOCALPORT", default=8000)

    mongo_user: str = Field(alias="MONGO_USER", default="admin")
    mongo_password: str = Field(alias="MONGO_PASSWORD", default="password123")
    mongo_host: str = Field(alias="MONGO_HOST", default="localhost")
    mongo_port: int = Field(alias="MONGO_PORT", default="27017")
    mongo_db_name: str = Field(alias="MONGO_DB_NAME", default="messageDB")


settings = Settings()
