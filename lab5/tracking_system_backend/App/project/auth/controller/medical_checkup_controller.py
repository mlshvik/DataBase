from flask import Blueprint, request, jsonify
from App.project.auth.service.medical_checkup_service import MedicalCheckupService

medical_checkup_bp = Blueprint('medical_checkup_bp', __name__)
service = MedicalCheckupService()

@medical_checkup_bp.route('/medical_checkups', methods=['GET'])
def get_checkups():
    checkups = service.get_all_checkups()
    return jsonify([c.to_dict() for c in checkups]), 200

@medical_checkup_bp.route('/medical_checkups/<int:checkup_id>', methods=['GET'])
def get_checkup_by_id(checkup_id):
    checkup = service.get_checkup_by_id(checkup_id)
    if checkup:
        return jsonify(checkup.to_dict()), 200
    return jsonify({'error': 'Medical checkup not found'}), 404

@medical_checkup_bp.route('/medical_checkups', methods=['POST'])
def create_checkup():
    data = request.get_json()
    if not data or not all(key in data for key in ['date', 'health_status', 'blood_pressure', 'heart_rate', 'Driver_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    checkup = service.create_checkup(data)
    return jsonify(checkup.to_dict()), 201

@medical_checkup_bp.route('/medical_checkups/<int:checkup_id>', methods=['PUT'])
def update_checkup(checkup_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    checkup = service.update_checkup(checkup_id, data)
    if checkup:
        return jsonify(checkup.to_dict()), 200
    return jsonify({'error': 'Medical checkup not found'}), 404

@medical_checkup_bp.route('/medical_checkups/<int:checkup_id>', methods=['DELETE'])
def delete_checkup(checkup_id):
    if service.delete_checkup(checkup_id):
        return ('', 204)
    return jsonify({'error': 'Medical checkup not found'}), 404
