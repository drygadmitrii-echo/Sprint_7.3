import pytest
import allure
from helpers.helper import register_new_courier, delete_courier
from api.courier_api import CourierAPI

@pytest.fixture
@allure.step("Создание и удаление тестового курьера")
def create_and_delete_courier():
    courier_api = CourierAPI()
    courier_data = register_new_courier()
    yield courier_data

    login_response = courier_api.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
