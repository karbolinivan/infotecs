import os
from enum import Enum


class Path(Enum):
    WEB_CALCULATOR = os.path.join(os.getcwd(), "webcalculator.exe")
    ENV = os.path.join(os.getcwd(), ".env")

    def __str__(self) -> str:
        return self.value
