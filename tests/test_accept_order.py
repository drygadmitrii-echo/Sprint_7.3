import pytest
import allure
from helpers.helper import register_new_courier, create_new_order, get_order_id_by_track
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from data.data import ERROR_MESSAGES

@allure.feature("Принятие заказа")
class TestAcceptOrder:
    courier_api = CourierAPI()
    order_api = OrderAPI()

    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        login_response = self.courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]

        order_response = create_new_order()
        assert order_response.status_code == 201
        track_id = order_response.json()["track"]

        order_id = get_order_id_by_track(track_id)
        assert order_id is not None

        response = self.order_api.accept_order(order_id, courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Принятие заказа без ID курьера")
    def test_accept_order_without_courier_id(self):
        order_response = create_new_order()
        assert order_response.status_code == 201
        track_id = order_response.json()["track"]

        order_id = get_order_id_by_track(track_id)
        assert order_id is not None

        response = self.order_api.accept_order(order_id, None)
        assert response.status_code == 400
        assert ERROR_MESSAGES["not_enough_search_data"] in response.json()["message"]

    @allure.title("Принятие несуществующего заказа")
    def test_accept_order_invalid_order_id(self):
        courier_data = register_new_courier()
        assert courier_data is not None

        login_response = self.courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]

        response = self.order_api.accept_order(999999, courier_id)
        assert response.status_code == 404
        assert "message" in response.json()
