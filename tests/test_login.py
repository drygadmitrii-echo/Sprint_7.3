import pytest
import allure
from helpers.helper import register_new_courier, generate_random_string
from api.courier_api import CourierAPI
from data.data import ERROR_MESSAGES

@allure.feature("Логин курьера")
class TestCourierLogin:
    courier_api = CourierAPI()

    @allure.title("Успешный логин курьера")
    def test_login_success(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин без логина")
    def test_login_without_login(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        payload = {"password": courier_data["password"]}
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_login_data"] in response.json()["message"]

    @allure.title("Логин без пароля")
    def test_login_without_password(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        payload = {"login": courier_data["login"]}
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_login_data"] in response.json()["message"]

    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_password(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        payload = {
            "login": courier_data["login"],
            "password": "wrong_password"
        }
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 404
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]

    @allure.title("Логин с неверным логином")
    def test_login_with_wrong_login(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        payload = {
            "login": "wrong_login",
            "password": courier_data["password"]
        }
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 404
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]

    @allure.title("Логин несуществующего пользователя")
    def test_login_nonexistent_user(self):
        payload = {
            "login": "nonexistent_user",
            "password": "nonexistent_password"
        }
        response = self.courier_api.login_courier(payload)
        assert response.status_code == 404
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]
