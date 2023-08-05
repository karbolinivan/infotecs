from enum import Enum
from src.service.settings import app_settings


class Endpoints(Enum):
    BASE_URL = f"http://{app_settings.host}:{app_settings.port}/api"
    STATE = "/state"
    ADDITION = "/addition"
    MULTIPLICATION = "/multiplication"
    DIVISION = "/division"
    REMAINDER = "/remainder"

    def __str__(self) -> str:
        return self.value
