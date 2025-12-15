from App.project.auth.domain.vehicle import Vehicle
from App.project.extension import db

class VehicleDAO:
    def get_all_vehicles(self):
        return Vehicle.query.all()

    def get_vehicle_by_id(self, vehicle_id):
        return Vehicle.query.get(vehicle_id)

    def create_vehicle(self, data):
        new_vehicle = Vehicle(
            type=data['type'],
            model=data['model'],
            capacity=data['capacity'],
            vehicle_numbers=data['vehicle_numbers'],
            quarry_id=data['Quarry_id']
        )
        db.session.add(new_vehicle)
        db.session.commit()
        return new_vehicle

    def update_vehicle(self, vehicle_id, data):
        vehicle = Vehicle.query.get(vehicle_id)
        if vehicle:
            vehicle.type = data.get('type', vehicle.type)
            vehicle.model = data.get('model', vehicle.model)
            vehicle.capacity = data.get('capacity', vehicle.capacity)
            vehicle.vehicle_numbers = data.get('vehicle_numbers', vehicle.vehicle_numbers)
            vehicle.quarry_id = data.get('Quarry_id', vehicle.quarry_id)
            db.session.commit()
            return vehicle
        return None

    def delete_vehicle(self, vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return True
        return False
