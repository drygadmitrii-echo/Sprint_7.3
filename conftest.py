import pytest
from helpers.helper import register_new_courier
import requests


@pytest.fixture
def create_courier():
    payload, login, password, first_name = register_new_courier()
    response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)
    assert response.status_code == 201

    yield payload

    # Удаление курьера после теста
    login_response = requests.post(
        "http://qa-scooter.praktikum-services.ru/api/v1/courier/login",
        json={"login": login, "password": password}
    )
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"http://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")
