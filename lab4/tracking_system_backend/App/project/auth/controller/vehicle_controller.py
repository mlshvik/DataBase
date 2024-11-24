from flask import Blueprint, request, jsonify
from App.project.auth.service.vehicle_service import VehicleService
vehicle_bp = Blueprint('vehicle_bp', __name__)
service = VehicleService()

@vehicle_bp.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = service.get_all_vehicles()
    return jsonify([v.to_dict() for v in vehicles]), 200

@vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = service.get_vehicle_by_id(vehicle_id)
    if vehicle:
        return jsonify(vehicle.to_dict()), 200
    return jsonify({'error': 'Vehicle not found'}), 404

@vehicle_bp.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    if not data or not all(key in data for key in ['type', 'model', 'capacity', 'vehicle_numbers', 'Quarry_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    vehicle = service.create_vehicle(data)
    return jsonify(vehicle.to_dict()), 201

@vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    vehicle = service.update_vehicle(vehicle_id, data)
    if vehicle:
        return jsonify(vehicle.to_dict()), 200
    return jsonify({'error': 'Vehicle not found'}), 404

@vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    if service.delete_vehicle(vehicle_id):
        return ('', 204)
    return jsonify({'error': 'Vehicle not found'}), 404
