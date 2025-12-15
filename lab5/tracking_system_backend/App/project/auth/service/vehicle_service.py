from App.project.auth.dao.vehicle_dao import VehicleDAO

class VehicleService:
    def __init__(self):
        self.dao = VehicleDAO()

    def get_all_vehicles(self):
        return self.dao.get_all_vehicles()

    def get_vehicle_by_id(self, vehicle_id):
        return self.dao.get_vehicle_by_id(vehicle_id)

    def create_vehicle(self, data):
        return self.dao.create_vehicle(data)

    def update_vehicle(self, vehicle_id, data):
        return self.dao.update_vehicle(vehicle_id, data)

    def delete_vehicle(self, vehicle_id):
        return self.dao.delete_vehicle(vehicle_id)
