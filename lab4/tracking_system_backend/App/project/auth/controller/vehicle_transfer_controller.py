from flask import Blueprint, request, jsonify
from App.project.auth.service.vehicle_transfer_service import VehicleTransferService


vehicle_transfer_bp = Blueprint('vehicle_transfer_bp', __name__)
service = VehicleTransferService()

@vehicle_transfer_bp.route('/vehicle_transfers', methods=['GET'])
def get_transfers():
    transfers = service.get_all_transfers()
    return jsonify([t.to_dict() for t in transfers]), 200

@vehicle_transfer_bp.route('/vehicle_transfers/<int:transfer_id>', methods=['GET'])
def get_transfer_by_id(transfer_id):
    transfer = service.get_transfer_by_id(transfer_id)
    if transfer:
        return jsonify(transfer.to_dict()), 200
    return jsonify({'error': 'Vehicle transfer not found'}), 404

@vehicle_transfer_bp.route('/vehicle_transfers', methods=['POST'])
def create_transfer():
    data = request.get_json()
    if not data or not all(key in data for key in ['transfer_date', 'Vehicle_id', 'Quarry_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    transfer = service.create_transfer(data)
    return jsonify(transfer.to_dict()), 201

@vehicle_transfer_bp.route('/vehicle_transfers/<int:transfer_id>', methods=['PUT'])
def update_transfer(transfer_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    transfer = service.update_transfer(transfer_id, data)
    if transfer:
        return jsonify(transfer.to_dict()), 200
    return jsonify({'error': 'Vehicle transfer not found'}), 404

@vehicle_transfer_bp.route('/vehicle_transfers/<int:transfer_id>', methods=['DELETE'])
def delete_transfer(transfer_id):
    if service.delete_transfer(transfer_id):
        return ('', 204)
    return jsonify({'error': 'Vehicle transfer not found'}), 404
