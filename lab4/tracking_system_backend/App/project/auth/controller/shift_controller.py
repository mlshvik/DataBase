from flask import Blueprint, request, jsonify
from App.project.auth.service.shift_service import ShiftService

shift_bp = Blueprint('shift_bp', __name__)
service = ShiftService()

@shift_bp.route('/shifts', methods=['GET'])
def get_shifts():
    shifts = service.get_all_shifts()
    return jsonify([s.to_dict() for s in shifts]), 200

@shift_bp.route('/shifts/<int:shift_id>', methods=['GET'])
def get_shift_by_id(shift_id):
    shift = service.get_shift_by_id(shift_id)
    if shift:
        return jsonify(shift.to_dict()), 200
    return jsonify({'error': 'Shift not found'}), 404

@shift_bp.route('/shifts', methods=['POST'])
def create_shift():
    data = request.get_json()
    if not data or not all(key in data for key in ['date', 'start_time', 'end_time', 'Vehicle_id', 'Driver_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    shift = service.create_shift(data)
    return jsonify(shift.to_dict()), 201

@shift_bp.route('/shifts/<int:shift_id>', methods=['PUT'])
def update_shift(shift_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    shift = service.update_shift(shift_id, data)
    if shift:
        return jsonify(shift.to_dict()), 200
    return jsonify({'error': 'Shift not found'}), 404

@shift_bp.route('/shifts/<int:shift_id>', methods=['DELETE'])
def delete_shift(shift_id):
    if service.delete_shift(shift_id):
        return ('', 204)
    return jsonify({'error': 'Shift not found'}), 404
