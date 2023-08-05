import allure
from pydantic import ValidationError
from src.enums.messages import AssertMessage


class Assertion:
    @staticmethod
    @allure.step("Checking status code")
    def status_code(actual, expected):
        try:
            assert actual == expected
        except AssertionError:
            raise AssertionError(f"\n{AssertMessage.STATUS_CODE}:"
                                 f"\nActual: {actual}"
                                 f"\nExpected: {expected}")

    @staticmethod
    @allure.step("Checking calculation result")
    def calculation_result(actual, expected):
        try:
            assert actual == expected
        except AssertionError:
            raise AssertionError(f"\n{AssertMessage.WRONG_RESULT}"
                                 f"\nActual result: {actual}"
                                 f"\nExpected result: {expected}")

    @staticmethod
    @allure.step("Checking server message")
    def message(actual, expected):
        try:
            assert actual == expected
        except AssertionError:
            raise AssertionError(f"\n{AssertMessage.INCORRECT_MESSAGE}"
                                 f"\nActual message: {actual}"
                                 f"\nExpected message: {expected}")

    @staticmethod
    @allure.step("Checking server message")
    def message_in(actual, expected):
        try:
            assert expected in actual
        except AssertionError:
            raise AssertionError(f"\n{AssertMessage.INCORRECT_MESSAGE}"
                                 f"\nActual message: {actual}"
                                 f"\nExpected message: {expected}")

    @staticmethod
    @allure.step("JSON validation against the model")
    def by_model(model, json):
        try:
            model(**json)
        except ValidationError as e:
            raise ValidationError(f"\n{AssertMessage.INVALID_MODEL}:\n{e.json()}")

    @staticmethod
    @allure.step("JSON key validation")
    def by_key(actual, key_list: list):
        try:
            for value in key_list:
                assert value in actual
        except ValidationError as e:
            raise ValidationError(f"\n{AssertMessage.INVALID_MODEL}:\n{e.json()}")


assertion = Assertion()
