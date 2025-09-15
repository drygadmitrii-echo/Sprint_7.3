import pytest
import requests
from helpers.helper import register_new_courier, create_new_order, get_order_id_by_track


class TestAcceptOrder:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    def test_accept_order_success(self):
        # Создаем курьера
        courier_data = register_new_courier()
        assert courier_data is not None

        # Логинимся курьером
        login_response = requests.post(f"{self.BASE_URL}/courier/login", json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]

        # Создаем заказ
        order_response = create_new_order()
        assert order_response.status_code == 201
        track_id = order_response.json()["track"]

        # Получаем ID заказа по track
        order_id = get_order_id_by_track(track_id)
        assert order_id is not None

        # Принимаем заказ
        response = requests.put(f"{self.BASE_URL}/orders/accept/{order_id}", params={
            "courierId": courier_id
        })
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    def test_accept_order_without_courier_id(self):
        # Создаем заказ
        order_response = create_new_order()
        assert order_response.status_code == 201
        track_id = order_response.json()["track"]

        # Получаем ID заказа по track
        order_id = get_order_id_by_track(track_id)
        assert order_id is not None

        # Пытаемся принять заказ без courierId
        response = requests.put(f"{self.BASE_URL}/orders/accept/{order_id}")
        assert response.status_code == 400
        assert "Недостаточно данных для поиска" in response.json()["message"]

    def test_accept_order_invalid_order_id(self):
        # Создаем курьера
        courier_data = register_new_courier()
        assert courier_data is not None

        # Логинимся курьером
        login_response = requests.post(f"{self.BASE_URL}/courier/login", json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]

        # Пытаемся принять несуществующий заказ
        response = requests.put(f"{self.BASE_URL}/orders/accept/999999", params={
            "courierId": courier_id
        })
        assert response.status_code == 404
