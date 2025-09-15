import requests
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
    return None

def create_new_order():
    order_data = {
        "firstName": "Александр",
        "lastName": "Барон",
        "address": "Авиамоторная улица, 8А",
        "metroStation": 8,
        "phone": "+79206709875",
        "rentTime": 2,
        "deliveryDate": "2025-09-16",
        "comment": "И поживее!",
        "color": ["BLACK"]
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_data)
    return response

def get_order_id_by_track(track_id):
    response = requests.get(
        'https://qa-scooter.praktikum-services.ru/api/v1/orders/track',
        params={"t": track_id}
    )
    if response.status_code == 200:
        return response.json()["order"]["id"]
    return None
