import random


class Response:
    def __init__(self, response):
        self.response = response

    def get_status_code(self):
        return self.response.json().get("statusCode")

    def get_message(self):
        return self.response.json().get("statusMessage")

    def get_state(self):
        return self.response.json().get("state")

    def get_result(self):
        return self.response.json().get("result")

    def get_json(self):
        return self.response.json()

    def get_headers(self):
        return self.response.headers


class Helper:
    @staticmethod
    def get_numbers(x_type: str = None, y_type: str = None, x=None, y=None):
        if x is not None:
            x = x
        else:
            if x_type == "INT":
                x = random.randint(1, 100)
            elif x_type == "N_INT":
                x = random.randint(-100, -1)
            elif x_type == "ZERO":
                x = 0
            elif x_type == "N_FLOAT":
                x = random.uniform(-100.0, -0.1)
            elif x_type == "FLOAT":
                x = random.uniform(0.1, 100.0)

        if y is not None:
            y = y
        else:
            if y_type == "INT":
                y = random.randint(1, 100)
            elif y_type == "N_INT":
                y = random.randint(-100, -1)
            elif y_type == "ZERO":
                y = 0
            elif y_type == "N_FLOAT":
                y = random.uniform(-100.0, -0.1)
            elif y_type == "FLOAT":
                y = random.uniform(0.1, 100.0)

        data = {
            "x": x,
            "y": y
        }
        return data

    @staticmethod
    def get_invalid_dict(key: str = None):
        data = {}
        if key:
            data = {key: random.randint(-100, 100)}
        return data

    @staticmethod
    def get_result(case: dict, func: str):
        operators = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "//": lambda x, y: x // y,
            "%": lambda x, y: x % y
        }
        return operators[func](case["x"], case["y"])

    @staticmethod
    def get_dict(value):
        return value.value


helper = Helper()
