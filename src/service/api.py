import allure

from src.base.client import client
from src.enums.endpoints import Endpoints


class Webcalculator:
    def __init__(self):
        self.request = client

    @allure.step("Server status check")
    def state(self):
        return self.request.get(endpoint=Endpoints.STATE.value)

    @allure.step("Invalid request")
    def invalid(self):
        return self.request.get(endpoint="/invalid")

    @allure.step('Adding: {payload}')
    def addition(self, payload: dict):
        return self.request.post(endpoint=Endpoints.ADDITION.value, json=payload)

    @allure.step('Multiplication: {payload}')
    def multiplication(self, payload: dict):
        return self.request.post(endpoint=Endpoints.MULTIPLICATION.value, json=payload)

    @allure.step('Division: {payload}')
    def division(self, payload: dict):
        return self.request.post(endpoint=Endpoints.DIVISION.value, json=payload)

    @allure.step('Remainder: {payload}')
    def reminder(self, payload: dict):
        return self.request.post(endpoint=Endpoints.REMAINDER.value, json=payload)

    @allure.step("OPTIONS")
    def get_options(self):
        return self.request.options()


webcalculator = Webcalculator()
