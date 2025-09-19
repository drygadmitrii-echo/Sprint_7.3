import pytest
import allure
from helpers.helper import generate_random_string
from api.courier_api import CourierAPI
from data.data import ERROR_MESSAGES

@allure.feature("Создание курьера")
class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        courier_api = CourierAPI()
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = courier_api.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание дубликата курьера")
    def test_create_duplicate_courier(self):
        courier_api = CourierAPI()
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        courier_api.create_courier(payload)
        response = courier_api.create_courier(payload)
        assert response.status_code == 409
        assert ERROR_MESSAGES["login_already_used"] in response.json()["message"]

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        courier_api = CourierAPI()
        payload = {"password": generate_random_string(10), "firstName": generate_random_string(10)}
        response = courier_api.create_courier(payload)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_data"] in response.json()["message"]

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        courier_api = CourierAPI()
        payload = {"login": generate_random_string(10), "firstName": generate_random_string(10)}
        response = courier_api.create_courier(payload)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_data"] in response.json()["message"]

    @allure.title("Создание курьера без имени")
    def test_create_courier_without_firstname(self):
        courier_api = CourierAPI()
        payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = courier_api.create_courier(payload)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_data"] in response.json()["message"]
