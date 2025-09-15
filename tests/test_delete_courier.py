import pytest
import requests
from helpers.helper import register_new_courier


class TestDeleteCourier:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    def test_delete_courier_success(self):
        # Сначала создаем курьера
        courier_data = register_new_courier()
        assert courier_data is not None

        # Логинимся, чтобы получить ID
        login_response = requests.post(f"{self.BASE_URL}/login", json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        })

        # Проверяем успешный логин
        assert login_response.status_code == 200
        assert "id" in login_response.json()

        courier_id = login_response.json()["id"]

        # Удаляем курьера
        response = requests.delete(f"{self.BASE_URL}/{courier_id}")
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    def test_delete_courier_without_id(self):
        response = requests.delete(f"{self.BASE_URL}/")
        # В зависимости от реализации сервера, может возвращаться 404 или 400
        assert response.status_code in [400, 404]

    def test_delete_nonexistent_courier(self):
        response = requests.delete(f"{self.BASE_URL}/999999")
        assert response.status_code == 404
