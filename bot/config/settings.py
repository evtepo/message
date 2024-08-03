from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_url: str = Field(alias="API_URL", default="http://message_nginx:80/api/v1/messages")

    token: str = Field(alias="BOT_TOKEN", default="Place your token here")


settings = Settings()
