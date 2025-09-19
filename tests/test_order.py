import pytest
import allure
from api.order_api import OrderAPI

@allure.feature("Создание заказа")
class TestOrderCreation:
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с разными цветами: {color}")
    def test_create_order_with_different_colors(self, color):
        order_api = OrderAPI()
        payload = {
            "firstName": "Александр",
            "lastName": "Барон",
            "address": "Авиамоторная улица, 8А",
            "metroStation": 8,
            "phone": "+79206709875",
            "rentTime": 2,
            "deliveryDate": "2025-09-16",
            "comment": "И поживее!",
            "color": color
        }
        response = order_api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
