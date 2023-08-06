import allure
import pytest

from src.base.assertions import assertion
from src.base.helps import Response, helper
from src.enums.cases import Cases
from src.enums.messages import StatusCode, Message
from src.service.api import webcalculator
from src.service.models import State, Result, Status


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("State")
@pytest.mark.api
class TestStateAPI:
    @allure.suite("Server")
    @allure.title("Checking for a state request")
    @allure.description("Checking for a state request")
    @pytest.mark.smoke
    def test_state_request(self, start_stop_webcalculator):
        result = webcalculator.state()
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=State, json=response.get_json())
        assertion.message(actual=response.get_state(), expected=Message.STATE.value)

    @allure.suite("Server")
    @allure.title("Checking for a invalid request")
    @allure.description("Checking for a invalid request")
    @pytest.mark.negative
    def test_invalid_request(self):
        result = webcalculator.invalid()
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.INVALID_REQUEST_FORMAT.value)
        assertion.message_in(actual=response.get_message(), expected=Message.INVALID_REQUEST_FORMAT.value)


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("Addition")
@pytest.mark.api
class TestAdditionAPI:
    @allure.suite("Integer")
    @allure.title("Checking for an addition request with integer numbers")
    @allure.description("Checking for an addition request")
    @pytest.mark.smoke
    def test_addition_request(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="+"))

    @allure.suite("Not Integer")
    @allure.description("Checking the server response for non-integer numbers")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_FLOAT_Y_INT.value, Cases.X_FLOAT_Y_INT.value,
        Cases.X_INT_Y_FLOAT.value, Cases.X_FLOAT_Y_FLOAT.value,
        Cases.X_N_FLOAT_Y_INT.value, Cases.X_INT_Y_N_FLOAT.value,
        Cases.X_N_FLOAT_Y_N_FLOAT.value, Cases.X_INT_Y_STR.value,
        Cases.X_STR_Y_INT.value, Cases.X_STR_Y_STR.value,
    ])
    def test_not_integer_addition_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for non-integer numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Missing Keys")
    @allure.description("Checking the server response for missing keys")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_EMPTY.value, Cases.X_EMPTY_Y_INT.value, Cases.X_EMPTY_Y_EMPTY.value
    ])
    def test_missing_keys_addition_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for missing keys: {payload}")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Value Size")
    @allure.description("Checking the server response for large values")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_SIZE.value, Cases.X_SIZE_Y_INT.value, Cases.X_SIZE_Y_SIZE.value
    ])
    def test_value_size_addition_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for large values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("Multiplication")
@pytest.mark.api
class TestMultiplicationAPI:
    @allure.suite("Integer")
    @allure.title("Checking for an multiplication request with integer numbers")
    @allure.description("Checking for an Multiplication request")
    @pytest.mark.smoke
    def test_multiplication_request(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="*"))

    @allure.suite("Not Integer")
    @allure.description("Checking the server response for non-integer numbers")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_FLOAT_Y_INT.value, Cases.X_FLOAT_Y_INT.value,
        Cases.X_INT_Y_FLOAT.value, Cases.X_FLOAT_Y_FLOAT.value,
        Cases.X_N_FLOAT_Y_INT.value, Cases.X_INT_Y_N_FLOAT.value,
        Cases.X_N_FLOAT_Y_N_FLOAT.value, Cases.X_INT_Y_STR.value,
        Cases.X_STR_Y_INT.value, Cases.X_STR_Y_STR.value,
    ])
    def test_not_integer_multiplication_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for non-integer numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Missing Keys")
    @allure.description("Checking the server response for missing keys")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_EMPTY.value, Cases.X_EMPTY_Y_INT.value, Cases.X_EMPTY_Y_EMPTY.value
    ])
    def test_missing_keys_multiplication_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for missing keys: {payload}")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Value Size")
    @allure.description("Checking the server response for large values")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_SIZE.value, Cases.X_SIZE_Y_INT.value, Cases.X_SIZE_Y_SIZE.value
    ])
    def test_value_size_multiplication_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for large values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("Division")
@pytest.mark.api
class TestDivisionAPI:
    @allure.suite("Integer")
    @allure.title("Checking for an division request with integer numbers")
    @allure.description("Checking for an Multiplication request")
    @pytest.mark.smoke
    def test_division_request(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="//"))

    @allure.suite("Not Integer")
    @allure.description("Checking the server response for non-integer numbers")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_FLOAT_Y_INT.value, Cases.X_FLOAT_Y_INT.value,
        Cases.X_INT_Y_FLOAT.value, Cases.X_FLOAT_Y_FLOAT.value,
        Cases.X_N_FLOAT_Y_INT.value, Cases.X_INT_Y_N_FLOAT.value,
        Cases.X_N_FLOAT_Y_N_FLOAT.value, Cases.X_INT_Y_STR.value,
        Cases.X_STR_Y_INT.value, Cases.X_STR_Y_STR.value,
    ])
    def test_not_integer_division_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for non-integer numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Missing Keys")
    @allure.description("Checking the server response for missing keys")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_EMPTY.value, Cases.X_EMPTY_Y_INT.value, Cases.X_EMPTY_Y_EMPTY.value
    ])
    def test_missing_keys_division_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for missing keys: {payload}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Value Size")
    @allure.description("Checking the server response for large values")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_SIZE.value, Cases.X_SIZE_Y_INT.value, Cases.X_SIZE_Y_SIZE.value
    ])
    def test_value_size_division_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for large values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Zero Value")
    @allure.description("Checking the server response for zero value")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_D_Y_ZERO.value, Cases.X_ZERO_D_Y_ZERO.value, Cases.X_N_INT_D_Y_ZERO.value
    ])
    def test_zero_value_division_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for zero value: x={payload['x']} and y={payload['y']}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("Reminder")
@pytest.mark.api
class TestReminderAPI:
    @allure.suite("Integer")
    @allure.title("Checking for an reminderrequest with integer numbers")
    @allure.description("Checking for an Multiplication request")
    @pytest.mark.smoke
    def test_reminder_request(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="%"))

    @allure.suite("Not Integer")
    @allure.description("Checking the server response for non-integer numbers")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_FLOAT_Y_INT.value, Cases.X_FLOAT_Y_INT.value,
        Cases.X_INT_Y_FLOAT.value, Cases.X_FLOAT_Y_FLOAT.value,
        Cases.X_N_FLOAT_Y_INT.value, Cases.X_INT_Y_N_FLOAT.value,
        Cases.X_N_FLOAT_Y_N_FLOAT.value, Cases.X_INT_Y_STR.value,
        Cases.X_STR_Y_INT.value, Cases.X_STR_Y_STR.value,
    ])
    def test_not_integer_reminder_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for non-integer numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Missing Keys")
    @allure.description("Checking the server response for missing keys")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_EMPTY.value, Cases.X_EMPTY_Y_INT.value, Cases.X_EMPTY_Y_EMPTY.value
    ])
    def test_missing_keys_reminder_request(self, payload, message, statuscode):
        allure.dynamic.title(f"Checking the server response for missing keys: {payload}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Value Size")
    @allure.description("Checking the server response for large values")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_Y_SIZE.value, Cases.X_SIZE_Y_INT.value, Cases.X_SIZE_Y_SIZE.value
    ])
    def test_value_size_reminder_request(self, payload, message, statuscode):
        allure.dynamic.title(
            f"Checking the server response for large values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)

    @allure.suite("Zero Value")
    @allure.description("Checking the server response for zero value")
    @pytest.mark.negative
    @pytest.mark.parametrize("payload, message, statuscode", [
        Cases.X_INT_D_Y_ZERO.value, Cases.X_ZERO_D_Y_ZERO.value, Cases.X_N_INT_D_Y_ZERO.value
    ])
    def test_zero_value_reminder_request(self, payload, message, statuscode):
        allure.dynamic.title(f"Checking the server response for zero value: x={payload['x']} and y={payload['y']}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=statuscode.value)
        assertion.by_model(model=Status, json=response.get_json())
        assertion.message(actual=response.get_message(), expected=message.value)


@allure.epic("Webcalculator")
@allure.feature("API")
@allure.story("Options")
@pytest.mark.api
class TestOptionsAPI:
    @allure.suite("Server")
    @allure.title("Checking for a options request")
    @allure.description("Checking for a options request")
    @pytest.mark.smoke
    def test_options_request(self):
        result = webcalculator.get_options()
        response = Response(response=result)
        headers = response.get_headers()

        assertion.status_code(actual=result.status_code, expected=200)
        assertion.by_key(actual=headers, key_list=["Server", "Date", "Content-Length", "Access-Control-Request-Method", "Connection"])
