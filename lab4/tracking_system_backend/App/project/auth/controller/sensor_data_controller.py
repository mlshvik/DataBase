from flask import Blueprint, request, jsonify
from App.project.auth.service.sensor_data_service import SensorDataService

sensor_data_bp = Blueprint('sensor_data_bp', __name__)
service = SensorDataService()

@sensor_data_bp.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    sensor_data_list = service.get_all_sensor_data()
    return jsonify([sd.to_dict() for sd in sensor_data_list]), 200

@sensor_data_bp.route('/sensor_data/<int:sensor_data_id>', methods=['GET'])
def get_sensor_data_by_id(sensor_data_id):
    sensor_data = service.get_sensor_data_by_id(sensor_data_id)
    if sensor_data:
        return jsonify(sensor_data.to_dict()), 200
    return jsonify({'error': 'Sensor data not found'}), 404

@sensor_data_bp.route('/sensor_data', methods=['POST'])
def create_sensor_data():
    data = request.get_json()
    if not data or not all(key in data for key in ['timestamp', 'location', 'speed', 'driver_health_status', 'Vehicle_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    sensor_data = service.create_sensor_data(data)
    return jsonify(sensor_data.to_dict()), 201

@sensor_data_bp.route('/sensor_data/<int:sensor_data_id>', methods=['PUT'])
def update_sensor_data(sensor_data_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    sensor_data = service.update_sensor_data(sensor_data_id, data)
    if sensor_data:
        return jsonify(sensor_data.to_dict()), 200
    return jsonify({'error': 'Sensor data not found'}), 404

@sensor_data_bp.route('/sensor_data/<int:sensor_data_id>', methods=['DELETE'])
def delete_sensor_data(sensor_data_id):
    if service.delete_sensor_data(sensor_data_id):
        return ('', 204)
    return jsonify({'error': 'Sensor data not found'}), 404
