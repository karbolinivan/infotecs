from enum import Enum


class Endpoints(Enum):
    BASE_URL = "http://localhost:17678/"
    STATE = f"api/state"
    ADDITION = f"api/addition"
    MULTIPLICATION = f"api/multiplication"
    DIVISION = f"api/division"
    REMAINDER = f"api/remainder"

    def __str__(self) -> str:
        return self.value
