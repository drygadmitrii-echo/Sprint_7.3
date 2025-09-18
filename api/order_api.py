from api.base_api import BaseAPI
from api.endpoints import Endpoints

class OrderAPI(BaseAPI):
    def create_order(self, data):
        return self.post(Endpoints.create_order, json=data)
    
    def get_orders_list(self):
        return self.get(Endpoints.get_orders_list)
    
    def get_order_by_track(self, track_id):
        return self.get(Endpoints.accept_order_by_number, params={"t": track_id})
    
    def accept_order(self, order_id, courier_id):
        return self.put(f"{Endpoints.accept_order.replace(':id', str(order_id))}", 
                       params={"courierId": courier_id})
    
    def cancel_order(self, track_id):
        return self.put(Endpoints.cancel_order, params={"track": track_id})
