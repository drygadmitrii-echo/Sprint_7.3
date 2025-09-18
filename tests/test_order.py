import pytest
import allure
from helpers.helper import create_new_order
from api.order_api import OrderAPI
from data.data import ORDER_DATA

@allure.feature("Создание заказа")
class TestOrderCreation:
    order_api = OrderAPI()

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с разными цветами: {color}")
    def test_create_order_with_different_colors(self, color):
        payload = ORDER_DATA.copy()
        payload["color"] = color

        response = self.order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с черным цветом")
    def test_create_order_with_black_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["BLACK"]

        response = self.order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с серым цветом")
    def test_create_order_with_grey_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["GREY"]

        response = self.order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с обоими цветами")
    def test_create_order_with_both_colors(self):
        payload = ORDER_DATA.copy()
        payload["color"] = ["BLACK", "GREY"]

        response = self.order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        payload = ORDER_DATA.copy()
        payload["color"] = []

        response = self.order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
