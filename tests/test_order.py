import pytest
import requests
from helpers.helper import create_new_order
from data.data import ORDER_DATA


class TestOrderCreation:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        payload = ORDER_DATA.copy()
        payload["color"] = color

        response = requests.post(self.BASE_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_with_black_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["BLACK"]

        response = requests.post(self.BASE_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_with_grey_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["GREY"]

        response = requests.post(self.BASE_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_with_both_colors(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["BLACK", "GREY"]

        response = requests.post(self.BASE_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_without_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = []

        response = requests.post(self.BASE_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
