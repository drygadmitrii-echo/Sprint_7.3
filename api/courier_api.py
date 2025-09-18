from api.base_api import BaseAPI
from api.endpoints import Endpoints

class CourierAPI(BaseAPI):
    def create_courier(self, data):
        return self.post(Endpoints.create_courier, json=data)
    
    def login_courier(self, data):
        return self.post(Endpoints.login_courier, json=data)
    
    def delete_courier(self, courier_id):
        return self.delete(f"{Endpoints.delete_courier}{courier_id}")
