import pytest
import requests
from helpers.helper import register_new_courier, generate_random_string

class TestCourierCreation:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    def test_create_courier_success(self):
        courier_data = register_new_courier()
        assert courier_data is not None

    def test_create_duplicate_courier(self):
        # Сначала создаем курьера
        courier_data = register_new_courier()
        assert courier_data is not None

        # Пытаемся создать такого же курьера
        response = requests.post(self.BASE_URL, json=courier_data)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

    def test_create_courier_without_login(self):
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(self.BASE_URL, json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json()["message"]

    def test_create_courier_without_password(self):
        login = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(self.BASE_URL, json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json()["message"]

    def test_create_courier_without_firstname(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(self.BASE_URL, json=payload)
        # Сервер принимает запросы без firstName, поэтому ожидаем 201
        assert response.status_code == 201
        assert response.json() == {"ok": True}
