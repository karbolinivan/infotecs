from enum import Enum


class Message(Enum):
    # сообщения отличаются от документации
    STATE = "OК"
    CALCULATION_ERROR = "Ошибка вычисления"
    MISSING_KEYS = "Не указаны необходимые параметры"
    NOT_INTEGER = "Значения параметров должны быть целыми"
    VALUE_SIZE_EXCEEDED = "Превышены максимальные значения параметров"
    INVALID_REQUEST_FORMAT = "Не верное имя задачи или тип HTTP запроса"
    ALL_OKAY = "Все хорошо"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return super().__eq__(other)


class StatusCode(Enum):
    CALCULATION_ERROR = 8  # в документации статус код указан как 1
    MISSING_KEYS = 2
    NOT_INTEGER = 3
    VALUE_SIZE_EXCEEDED = 4
    INVALID_REQUEST_FORMAT = 5
    ALL_OKAY = 0

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return super().__eq__(other)


class AssertMessage(Enum):
    STATUS_CODE = "Status code does not match the expected value"
    WRONG_RESULT = "Incorrect calculation result"
    INCORRECT_MESSAGE = "Incorrect message received from the server"
    INVALID_MODEL = "The server's response does not match the model"
    START_WEB_CALCULATOR = "Веб-калькулятор запущен"
    STOP_WEB_CALCULATOR = "Веб-калькулятор остановлен"
    WEB_CALCULATOR_ALREADY_RUNNING = "Сервер уже запущен"

    def __str__(self) -> str:
        return self.value


class App(Enum):
    HOST = "local"
    PORT = "7777"

    def __str__(self):
        return self.value


class AppMessage(Enum):
    START_WEB_CALCULATOR = "Веб-калькулятор запущен"
    STOP_WEB_CALCULATOR = "Веб-калькулятор остановлен"
    WEB_CALCULATOR_ALREADY_RUNNING = "Сервер уже запущен"
    START_HOST = f"{START_WEB_CALCULATOR} на {App.HOST}"
    START_HOST_PORT = f"{START_WEB_CALCULATOR} на {App.HOST}:{App.PORT}"
    UNKNOWN_COMMAND = "(choose from 'start', 'stop', 'restart', 'show_log'"

    def __str__(self) -> str:
        return self.value
