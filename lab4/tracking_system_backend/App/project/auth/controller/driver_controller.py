from flask import Blueprint, request, jsonify
from App.project.auth.service.driver_service import DriverService

driver_bp = Blueprint('driver_bp', __name__)
service = DriverService()

@driver_bp.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = service.get_all_drivers()
    return jsonify([d.to_dict() for d in drivers]), 200

@driver_bp.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = service.get_driver_by_id(driver_id)
    if driver:
        return jsonify(driver.to_dict()), 200
    return jsonify({'error': 'Driver not found'}), 404

@driver_bp.route('/drivers', methods=['POST'])
def create_driver():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'license_number', 'experience_years', 'Company_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    driver = service.create_driver(data)
    return jsonify(driver.to_dict()), 201

@driver_bp.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    driver = service.update_driver(driver_id, data)
    if driver:
        return jsonify(driver.to_dict()), 200
    return jsonify({'error': 'Driver not found'}), 404

@driver_bp.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    if service.delete_driver(driver_id):
        return ('', 204)
    return jsonify({'error': 'Driver not found'}), 404
