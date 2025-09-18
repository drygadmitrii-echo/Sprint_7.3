import pytest
import allure
from helpers.helper import create_new_order
from api.order_api import OrderAPI
from data.data import ERROR_MESSAGES

@allure.feature("Получение заказа по номеру")
class TestGetOrder:
    order_api = OrderAPI()

    @allure.title("Успешное получение заказа по номеру")
    def test_get_order_by_track_success(self):
        order_response = create_new_order()
        order_track = order_response.json()["track"]

        response = self.order_api.get_order_by_track(order_track)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Получение заказа без номера")
    def test_get_order_without_track(self):
        response = self.order_api.get_order_by_track(None)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_search_data"] in response.json()["message"]

    @allure.title("Получение несуществующего заказа")
    def test_get_order_with_nonexistent_track(self):
        response = self.order_api.get_order_by_track(999999)
        assert response.status_code == 404
        assert ERROR_MESSAGES["order_not_found"] in response.json()["message"]
