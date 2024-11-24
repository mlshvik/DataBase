from flask import Blueprint, request, jsonify
from App.project.auth.service.driver_assignment_service import DriverAssignmentService

driver_assignment_bp = Blueprint('driver_assignment_bp', __name__)
service = DriverAssignmentService()

@driver_assignment_bp.route('/driver_assignments', methods=['GET'])
def get_assignments():
    assignments = service.get_all_assignments()
    return jsonify([a.to_dict() for a in assignments]), 200

@driver_assignment_bp.route('/driver_assignments/<int:assignment_id>', methods=['GET'])
def get_assignment_by_id(assignment_id):
    assignment = service.get_assignment_by_id(assignment_id)
    if assignment:
        return jsonify(assignment.to_dict()), 200
    return jsonify({'error': 'Driver assignment not found'}), 404

@driver_assignment_bp.route('/driver_assignments', methods=['POST'])
def create_assignment():
    data = request.get_json()
    if not data or not all(key in data for key in ['start_date', 'end_date', 'Driver_id', 'Vehicle_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    assignment = service.create_assignment(data)
    return jsonify(assignment.to_dict()), 201

@driver_assignment_bp.route('/driver_assignments/<int:assignment_id>', methods=['PUT'])
def update_assignment(assignment_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    assignment = service.update_assignment(assignment_id, data)
    if assignment:
        return jsonify(assignment.to_dict()), 200
    return jsonify({'error': 'Driver assignment not found'}), 404

@driver_assignment_bp.route('/driver_assignments/<int:assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    if service.delete_assignment(assignment_id):
        return ('', 204)
    return jsonify({'error': 'Driver assignment not found'}), 404
