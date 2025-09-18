import pytest
from helpers.helper import register_new_courier, delete_courier
from api.courier_api import CourierAPI

@pytest.fixture
def create_and_delete_courier():
    """Фикстура для создания и последующего удаления курьера"""
    courier_data = register_new_courier()
    
    yield courier_data
    
    # Логинимся для получения ID и удаления
    courier_api = CourierAPI()
    login_response = courier_api.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
