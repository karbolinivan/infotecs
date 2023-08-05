import allure
import pytest

from src.enums.cases import Cases
from src.service.api import webcalculator
from src.base.assertions import assertion
from src.enums.messages import StatusCode
from src.base.helps import Response, helper
from src.service.models import Result


@allure.epic("Webcalculator")
@allure.feature("Math Operations")
@allure.story("Addition")
@pytest.mark.functional
class TestAddition:
    @allure.suite("Positive Numbers")
    @allure.title("Checking the addition function with positive numbers")
    @allure.description("Checking the result of adding x and y")
    @pytest.mark.smoke
    def test_addition_positive_numbers(self, start_stop_webcalculator):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="+"))

    @allure.suite("Negative Numbers")
    @allure.title("Checking the addition function with negative numbers")
    @allure.description("Checking the result of adding x and y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_N_INT, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_INT, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_N_INT, func="+"),
    ])
    def test_addition_negative_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the addition function with negative numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)

    @allure.suite("Zero Numbers")
    @allure.title("Checking the addition function with zero values")
    @allure.description("Checking the result of adding x and y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_INT, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_ZERO, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_ZERO, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_ZERO, func="+"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_N_INT, func="+"),
    ])
    def test_addition_zero_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the addition function with zero values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.addition(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)


@allure.epic("Webcalculator")
@allure.feature("Math Operations")
@allure.story("Multiplication")
@pytest.mark.functional
class TestMultiplication:
    @allure.suite("Positive Numbers")
    @allure.title("Checking the multiplication function with positive numbers")
    @allure.description("Checking of the multiplication result of x and y")
    @pytest.mark.smoke
    def test_multiplication_positive_numbers(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="*"))

    @allure.suite("Negative Numbers")
    @allure.title("Checking the multiplication function with negative numbers")
    @allure.description("Checking of the multiplication result of x and y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_N_INT, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_INT, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_N_INT, func="*"),
    ])
    def test_multiplication_negative_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the multiplication function with negative numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)

    @allure.suite("Zero Numbers")
    @allure.title("Checking the multiplication function with zero values")
    @allure.description("Checking of the multiplication result of x and y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_INT, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_ZERO, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_ZERO, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_ZERO, func="*"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_N_INT, func="*"),
    ])
    def test_multiplication_zero_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the multiplication function with zero values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.multiplication(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)


@allure.epic("Webcalculator")
@allure.feature("Math Operations")
@allure.story("Division")
@pytest.mark.functional
class TestDivision:
    @allure.suite("Positive Numbers")
    @allure.title("Checking the division function with positive numbers")
    @allure.description("Checking the division of x by y")
    @pytest.mark.smoke
    def test_division_positive_numbers(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="//"))

    @allure.suite("Negative Numbers")
    @allure.title("Checking the division function with negative numbers")
    @allure.description("Checking the division of x by y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_N_INT, func="//"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_INT, func="//"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_N_INT, func="//"),
    ])
    def test_division_negative_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the multiplication function with negative numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)

    @allure.suite("Zero Numbers")
    @allure.title("Checking the division function with zero values")
    @allure.description("Checking the division of x by y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_INT, func="//"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_N_INT, func="//"),
    ])
    def test_division_zero_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the multiplication function with zero values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.division(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)


@allure.epic("Webcalculator")
@allure.feature("Math Operations")
@allure.story("Reminder")
@pytest.mark.functional
class TestReminder:
    @allure.suite("Positive Numbers")
    @allure.title("Checking the reminder function with positive numbers")
    @allure.description("Checking the reminder of x by y")
    @pytest.mark.smoke
    def test_reminder_positive_numbers(self):
        payload = helper.get_numbers(x_type="INT", y_type="INT")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=helper.get_result(case=payload, func="%"))

    @allure.suite("Negative Numbers")
    @allure.title("Checking the reminder function with negative numbers")
    @allure.description("Checking the reminder of x by y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_INT_Y_N_INT, func="%"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_INT, func="%"),
        Cases.get_calculation_parametrize(case=Cases.X_N_INT_Y_N_INT, func="%"),
    ])
    def test_reminder_negative_numbers(self, payload, calculate):
        allure.dynamic.title(
            f"Checking the reminder function with negative numbers: x={payload['x']} and y={payload['y']}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)

    @allure.suite("Zero Numbers")
    @allure.title("Checking the reminder function with zero values")
    @allure.description("Checking the reminder of x by y")
    @pytest.mark.parametrize("payload, calculate", [
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_INT, func="%"),
        Cases.get_calculation_parametrize(case=Cases.X_ZERO_Y_N_INT, func="%"),
    ])
    def test_reminder_zero_numbers(self, payload, calculate):
        allure.dynamic.title(f"Checking the reminder function with zero values: x={payload['x']} and y={payload['y']}")
        result = webcalculator.reminder(payload=payload)
        response = Response(response=result)

        assertion.status_code(actual=response.get_status_code(), expected=StatusCode.ALL_OKAY.value)
        assertion.by_model(model=Result, json=response.get_json())
        assertion.calculation_result(actual=response.get_result(), expected=calculate)
