import allure
import random
import string
from api.courier_api import CourierAPI
from api.order_api import OrderAPI

@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@allure.step("Регистрация нового курьера")
def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {"login": login, "password": password, "firstName": first_name}
    response = CourierAPI().create_courier(payload)

    if response.status_code == 201:
        return {"login": login, "password": password, "firstName": first_name}
    return None

@allure.step("Удаление курьера с ID {courier_id}")
def delete_courier(courier_id):
    return CourierAPI().delete_courier(courier_id)

@allure.step("Создание нового заказа")
def create_new_order(color=None):
    order_data = {
        "firstName": "Александр",
        "lastName": "Барон",
        "address": "Авиамоторная улица, 8А",
        "metroStation": 8,
        "phone": "+79206709875",
        "rentTime": 2,
        "deliveryDate": "2025-09-16",
        "comment": "И поживее!",
        "color": color if color else ["BLACK"]
    }
    return OrderAPI().create_order(order_data)

@allure.step("Получение ID заказа по трек-номеру {track_id}")
def get_order_id_by_track(track_id):
    response = OrderAPI().get_order_by_track(track_id)
    if response.status_code == 200:
        return response.json()["order"]["id"]
    return None
