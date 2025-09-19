import allure
from api.base_api import BaseAPI
from api.endpoints import Endpoints

class CourierAPI(BaseAPI):
    @allure.step("Создание курьера")
    def create_courier(self, data):
        return self.post(Endpoints.create_courier, json=data)

    @allure.step("Логин курьера")
    def login_courier(self, data):
        return self.post(Endpoints.login_courier, json=data)

    @allure.step("Удаление курьера с ID {courier_id}")
    def delete_courier(self, courier_id):
        return self.delete(f"{Endpoints.delete_courier}{courier_id}")
