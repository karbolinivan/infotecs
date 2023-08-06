from pydantic_settings import BaseSettings
from src.enums.paths import Path


class Settings(BaseSettings):
    host: str = "localhost"
    port: str = "9999"
    file: str = "webcalculator.exe"
    start: str = "start"
    stop: str = "stop"
    restart: str = "restart"

    # class Config:
    #     env_file = f"{Path.ENV}"
    #     env_file_encoding = "utf-8"


app_settings = Settings()
