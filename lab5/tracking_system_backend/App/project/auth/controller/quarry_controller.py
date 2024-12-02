from flask import Blueprint, request, jsonify
from App.project.auth.service.quarry_service import QuarryService

quarry_bp = Blueprint('quarry_bp', __name__)
service = QuarryService()

@quarry_bp.route('/quarries', methods=['GET'])
def get_quarries():
    quarries = service.get_all_quarries()
    return jsonify([q.to_dict() for q in quarries]), 200

@quarry_bp.route('/quarries/<int:quarry_id>', methods=['GET'])
def get_quarry(quarry_id):
    quarry = service.get_quarry_by_id(quarry_id)
    if quarry:
        return jsonify(quarry.to_dict()), 200
    return jsonify({'error': 'Quarry not found'}), 404

@quarry_bp.route('/quarries', methods=['POST'])
def create_quarry():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'location', 'operation_hours', 'Company_id']):
        return jsonify({'error': 'Invalid input data'}), 400

    quarry = service.create_quarry(data)
    return jsonify(quarry.to_dict()), 201

@quarry_bp.route('/quarries/<int:quarry_id>', methods=['PUT'])
def update_quarry(quarry_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    quarry = service.update_quarry(quarry_id, data)
    if quarry:
        return jsonify(quarry.to_dict()), 200
    return jsonify({'error': 'Quarry not found'}), 404

@quarry_bp.route('/quarries/<int:quarry_id>', methods=['DELETE'])
def delete_quarry(quarry_id):
    if service.delete_quarry(quarry_id):
        return ('', 204)
    return jsonify({'error': 'Quarry not found'}), 404


@quarry_bp.route('/quarries/dummy', methods=['POST'])
def insert_dummy_quarries():
    """Обробляє POST-запит для вставки тестових даних у таблицю Quarry."""
    try:
        service.insert_dummy_quarries()
        return jsonify({'message': 'Dummy quarries inserted successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500