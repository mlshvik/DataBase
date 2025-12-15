from flask import Blueprint, request, jsonify
from App.project.auth.service.maintenance_service import MaintenanceService

maintenance_bp = Blueprint('maintenance_bp', __name__)
service = MaintenanceService()

@maintenance_bp.route('/maintenance', methods=['GET'])
def get_maintenance_records():
    maintenance_records = service.get_all_maintenance_records()
    return jsonify([m.to_dict() for m in maintenance_records]), 200

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['GET'])
def get_maintenance_record_by_id(maintenance_id):
    maintenance_record = service.get_maintenance_record_by_id(maintenance_id)
    if maintenance_record:
        return jsonify(maintenance_record.to_dict()), 200
    return jsonify({'error': 'Maintenance record not found'}), 404

@maintenance_bp.route('/maintenance', methods=['POST'])
def create_maintenance_record():
    data = request.get_json()
    if not data or not all(key in data for key in ['date', 'description', 'status', 'Vehicle_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    maintenance_record = service.create_maintenance_record(data)
    return jsonify(maintenance_record.to_dict()), 201

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['PUT'])
def update_maintenance_record(maintenance_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    maintenance_record = service.update_maintenance_record(maintenance_id, data)
    if maintenance_record:
        return jsonify(maintenance_record.to_dict()), 200
    return jsonify({'error': 'Maintenance record not found'}), 404

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['DELETE'])
def delete_maintenance_record(maintenance_id):
    if service.delete_maintenance_record(maintenance_id):
        return ('', 204)
    return jsonify({'error': 'Maintenance record not found'}), 404
