import requests
import allure
from tests.urls import Urls

class BaseAPI:
    def __init__(self):
        self.base_url = Urls.QA_SCOOTER_URL

    @allure.step("Отправка POST запроса на {endpoint}")
    def post(self, endpoint, json=None, params=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, params=params)

    @allure.step("Отправка GET запроса на {endpoint}")
    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    @allure.step("Отправка PUT запроса на {endpoint}")
    def put(self, endpoint, json=None, params=None):
        return requests.put(f"{self.base_url}{endpoint}", json=json, params=params)

    @allure.step("Отправка DELETE запроса на {endpoint}")
    def delete(self, endpoint, params=None):
        return requests.delete(f"{self.base_url}{endpoint}", params=params)
