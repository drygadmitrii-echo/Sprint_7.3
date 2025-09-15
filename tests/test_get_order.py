import pytest
import requests
from helpers.helper import create_new_order


class TestGetOrder:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    def test_get_order_by_track_success(self):
        order_response = create_new_order()
        order_track = order_response.json()["track"]

        response = requests.get(f"{self.BASE_URL}/track", params={"t": order_track})

        assert response.status_code == 200
        assert "order" in response.json()

    def test_get_order_without_track(self):
        response = requests.get(f"{self.BASE_URL}/track")

        assert response.status_code == 400
        assert "Недостаточно данных для поиска" in response.json()["message"]

    def test_get_order_with_nonexistent_track(self):
        response = requests.get(f"{self.BASE_URL}/track", params={"t": 999999})

        assert response.status_code == 404
        assert "Заказ не найден" in response.json()["message"]
