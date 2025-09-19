import pytest
import allure
from helpers.helper import register_new_courier, delete_courier
from api.courier_api import CourierAPI
from data.data import ERROR_MESSAGES

@allure.feature("Удаление курьера")
class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self):
        courier_api = CourierAPI()
        courier_data = register_new_courier()
        login_response = courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json()["id"]
        response = delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Удаление курьера без ID")
    def test_delete_courier_without_id(self):
        response = CourierAPI().delete_courier("")
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Удаление несуществующего курьера")
    def test_delete_nonexistent_courier(self):
        response = CourierAPI().delete_courier("999999")
        assert response.status_code == 404
        assert "message" in response.json()
