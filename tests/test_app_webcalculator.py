import allure
import pytest

from src.base.assertions import assertion

from src.enums.messages import AppMessage, App


@allure.epic("Webcalculator")
@allure.feature("Application")
@allure.suite("Management")
@pytest.mark.app
class TestApplication:
    @allure.title("Testing application startup and shutdown")
    @allure.description("Application startup and shutdown test with default settings")
    @pytest.mark.smoke
    def test_application_start(self, start_webcalculator_app):
        app = start_webcalculator_app

        start = app.up(default=True)
        message_start = start.stdout
        assertion.message_in(actual=message_start, expected=AppMessage.START_WEB_CALCULATOR.value)

        start = app.down()
        message_stop = start.stdout
        assertion.message_in(actual=message_stop, expected=AppMessage.STOP_WEB_CALCULATOR.value)

    @allure.title("Testing application restart")
    @allure.description("Application restart test with default settings")
    def test_application_restart(self, start_stop_webcalculator_app):
        app = start_stop_webcalculator_app
        restart = app.command(command="restart")

        message = restart.stdout
        assertion.message_in(actual=message, expected=AppMessage.START_WEB_CALCULATOR.value)

    @allure.title("Checking if the application is already running")
    @allure.description("Application is already running test with default settings")
    def test_application_already_start(self, start_stop_webcalculator_app):
        app = start_stop_webcalculator_app
        start = app.up(default=True)

        message = start.stdout
        assertion.message_in(actual=message, expected=AppMessage.WEB_CALCULATOR_ALREADY_RUNNING.value)

    @allure.description("Application startup and shutdown test with host")
    def test_application_start_host(self, start_webcalculator_app):
        app = start_webcalculator_app
        start = app.up(default=True, host=App.HOST.value)

        message = start.stdout
        assertion.message_in(actual=message, expected=AppMessage.START_HOST.value)

        app.down()
        allure.dynamic.title(f"Testing application startup and shutdown with host: {App.HOST}")

    @allure.description("Application startup and shutdown test with host")
    def test_application_start_host_port(self, start_webcalculator_app):
        app = start_webcalculator_app
        start = app.up(host=App.HOST.value, port=App.PORT.value)

        message = start.stdout
        assertion.message_in(actual=message, expected=AppMessage.START_HOST_PORT.value)

        app.down()
        allure.dynamic.title(f"Testing application startup and shutdown with host and port: {App.HOST}:{App.PORT}")

    @allure.title("Checking the show log command")
    @allure.description("Checking the show log command")
    def test_application_show_log(self, start_stop_webcalculator_app):
        app = start_stop_webcalculator_app
        show_log = app.command(command="-h")

        statuscode = show_log.returncode
        assertion.status_code(actual=statuscode, expected=0)

    @allure.title("Checking the unknown command")
    @allure.description("Checking the unknown command")
    def test_application_unknown(self, start_stop_webcalculator_app):
        app = start_stop_webcalculator_app
        command = app.command(command="unknown")

        message = command.stderr
        assertion.message_in(actual=message, expected=AppMessage.UNKNOWN_COMMAND.value)
