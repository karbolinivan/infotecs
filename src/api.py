from src.base.client import client
from src.enum import Endpoints


class Calculator:
    def __init__(self):
        self.request = client

    def state(self):
        return self.request.get(endpoint=Endpoints.STATE)

    def addition(self, payload, data=None):
        return self.request.post(endpoint=Endpoints.ADDITION, json=payload, data=data)

    def multiplication(self, payload, data=None):
        return self.request.post(endpoint=Endpoints.MULTIPLICATION, json=payload, data=data)

    def division(self, payload, data=None):
        return self.request.post(endpoint=Endpoints.DIVISION, json=payload, data=data)

    def reminder(self, payload, data=None):
        return self.request.post(endpoint=Endpoints.REMAINDER, json=payload, data=data)

    def get_options(self):
        return self.request.options()
