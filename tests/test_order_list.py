import pytest
import allure
from api.order_api import OrderAPI

@allure.feature("Список заказов")
class TestOrderList:
    order_api = OrderAPI()

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = self.order_api.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
