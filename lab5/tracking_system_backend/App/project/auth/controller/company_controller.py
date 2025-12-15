from flask import Blueprint, request, jsonify
from App.project.auth.service.company_service import CompanyService
import logging
company_bp = Blueprint('company_bp', __name__)
service = CompanyService()

@company_bp.route('/companies', methods=['GET'])
def get_companies():
    try:
        companies = service.get_all_companies()
        return jsonify([c.to_dict() for c in companies]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@company_bp.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    try:
        company = service.get_company_by_id(company_id)
        if company:
            return jsonify(company.to_dict()), 200
        else:
            return jsonify({'error': 'Company not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@company_bp.route('/companies', methods=['POST'])
def create_company():
    data = request.get_json()
    logging.debug(f"Received data: {data}")
    if not data or not all(key in data for key in ['name', 'address', 'contact_info']):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        company = service.create_company(data)
        return jsonify(company.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@company_bp.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'address', 'contact_info']):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        company = service.update_company(company_id, data)
        if company:
            return jsonify(company.to_dict()), 200
        else:
            return jsonify({'error': 'Company not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@company_bp.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    try:
        if service.delete_company(company_id):
            return ('', 204)
        else:
            return jsonify({'error': 'Company not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
