import allure
import random
import string
from api.courier_api import CourierAPI
from api.order_api import OrderAPI

@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step("Регистрация нового курьера")
def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    courier_api = CourierAPI()
    response = courier_api.create_courier(payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
    return None

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

    order_api = OrderAPI()
    return order_api.create_order(order_data)

@allure.step("Получение ID заказа по track номеру {track_id}")
def get_order_id_by_track(track_id):
    order_api = OrderAPI()
    response = order_api.get_order_by_track(track_id)
    if response.status_code == 200:
        return response.json()["order"]["id"]
    return None

@allure.step("Удаление курьера с ID {courier_id}")
def delete_courier(courier_id):
    courier_api = CourierAPI()
    return courier_api.delete_courier(courier_id)
