import pytest
import allure
from api.order_api import OrderAPI

@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        order_api = OrderAPI()
        response = order_api.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
