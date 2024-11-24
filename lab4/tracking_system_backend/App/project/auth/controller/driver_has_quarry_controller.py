from flask import Blueprint, request, jsonify
from App.project.auth.service.driver_has_quarry_service import DriverHasQuarryService

driver_has_quarry_bp = Blueprint('driver_has_quarry_bp', __name__)
service = DriverHasQuarryService()

@driver_has_quarry_bp.route('/driver_has_quarries', methods=['GET'])
def get_all_assignments():
    assignments = service.get_all_assignments()
    return jsonify([a.to_dict() for a in assignments]), 200

@driver_has_quarry_bp.route('/driver_has_quarries', methods=['POST'])
def add_assignment():
    data = request.get_json()
    if not data or not all(key in data for key in ['Driver_id', 'Quarry_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    assignment = service.add_assignment(data)
    return jsonify(assignment.to_dict()), 201

@driver_has_quarry_bp.route('/driver_has_quarries/<int:driver_id>/<int:quarry_id>', methods=['DELETE'])
def delete_assignment(driver_id, quarry_id):
    if service.delete_assignment(driver_id, quarry_id):
        return ('', 204)
    return jsonify({'error': 'Assignment not found'}), 404
