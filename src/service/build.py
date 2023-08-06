import subprocess
import allure

from src.enums.paths import Path
from src.service.settings import app_settings


class Build:
    def __init__(self, settings=None):
        self._settings = settings
        self._settings = settings if settings is not None else app_settings
        self._host = self._settings.host
        self._port = self._settings.port
        self._file = f"{Path.WEB_CALCULATOR}"

    @allure.step("Start webcalculator")
    def up(self, host: str = None, port: str = None, default: bool = False):
        args = ["cmd", "/c", self._file, "start"]

        if default:
            self._host = None
            self._port = None

        if host:
            self._host = host
            if port:
                self._port = port

        if self._host:
            args.append(self._host)
            if self._port:
                args.append(self._port)

        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result

    @allure.step("Stop webcalculator")
    def down(self):
        args = ["cmd", "/c", self._file, "stop"]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result

    @allure.step("Restart webcalculator")
    def restart(self):
        args = ["cmd", "/c", self._file, "restart"]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result

    @allure.step("Command webcalculator {command}")
    def command(self, command: str):
        args = ["cmd", "/c", self._file, command]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result
