import allure
import requests
from requests import Response

from src.base.logs import log
from src.enums.endpoints import Endpoints


class Request:
    def __init__(self, base_url, headers=None, cookie=None, auth=None):
        self.base_url = base_url
        self.headers = headers
        self.cookie = cookie
        self.auth = auth

    @allure.step("GET request to: {endpoint}")
    def get(self, endpoint, params=None) -> Response:
        url = f'{self.base_url}{endpoint}'
        log.save_request(method="POST", url=url, auth=self.auth, headers=self.headers, cookies=self.cookie)
        response = requests.get(url=url, params=params, auth=self.auth, headers=self.headers, cookies=self.cookie)
        log.save_response(response=response)
        return response

    @allure.step("POST request to: {endpoint}")
    def post(self, endpoint, json=None, data=None) -> Response:
        url = f'{self.base_url}{endpoint}'
        log.save_request(method="POST", url=url, auth=self.auth, headers=self.headers, cookies=self.cookie, json=json, data=data)
        response = requests.post(url=url, auth=self.auth, headers=self.headers, cookies=self.cookie, json=json, data=data)
        log.save_response(response=response)
        return response

    @allure.step("Requests OPTIONS")
    def options(self) -> Response:
        url = f'{self.base_url}api'
        log.save_request(method="POST", url=url, auth=self.auth, headers=self.headers, cookies=self.cookie)
        response = requests.options(url=url, auth=self.auth, headers=self.headers, cookies=self.cookie)
        log.save_response(response=response)
        return response


client = Request(base_url=Endpoints.BASE_URL)
