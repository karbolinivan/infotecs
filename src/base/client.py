import allure
import requests
from requests import Response

from src.enum import Endpoints


class Request:
    def __init__(self, base_url, headers=None, cookie=None, auth=None):
        self.base_url = base_url
        self.headers = headers
        self.cookie = cookie
        self.auth = auth

    @allure.step("GET request to:\n{url}")
    def get(self, endpoint, params=None) -> Response:
        url = f'{self.base_url}{endpoint}'
        print(url)
        response = requests.get(url=url, params=params, auth=self.auth, headers=self.headers, cookies=self.cookie)
        return response

    @allure.step("POST request to:\n{url}")
    def post(self, endpoint, json=None, data=None) -> Response:
        url = f'{self.base_url}{endpoint}'
        response = requests.post(url=url, auth=self.auth, headers=self.headers, cookies=self.cookie, json=json,
                                 data=data)
        return response

    @allure.step("OPTIONS request to:\n{url}")
    def options(self) -> Response:
        url = f'{self.base_url}api'
        response = requests.options(url=url, auth=self.auth, headers=self.headers, cookies=self.cookie)
        return response


client = Request(base_url=Endpoints.BASE_URL)
