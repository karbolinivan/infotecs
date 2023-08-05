from pydantic_settings import BaseSettings
from src.enums.paths import Path


class Settings(BaseSettings):
    host: str
    port: str
    file: str
    start: str
    stop: str
    restart: str

    class Config:
        env_file = f"{Path.ENV}"
        env_file_encoding = "utf-8"


app_settings = Settings()
