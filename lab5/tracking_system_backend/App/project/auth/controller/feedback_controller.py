from flask import Blueprint, request, jsonify
from datetime import datetime
from App.project.auth.service.feedback_service import FeedbackService
import logging

feedback_bp = Blueprint('feedback_bp', __name__)
service = FeedbackService()


@feedback_bp.route('/feedbacks', methods=['GET'])
def get_companies():
    try:
        companies = service.get_all_feedbacks()
        return jsonify([c.to_dict() for c in companies]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@feedback_bp.route('/feedbacks', methods=['POST'])
def create_company():
    data = request.get_json()
    logging.debug(f"Received data: {data}")
    if not data or not all(key in data for key in ['comment', 'rating', "driver_id"]):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        data["feedback_date"] = datetime.now().strftime('%Y-%m-%d')
        feedbacks = service.create_and_get_all_feedbacks(data)
        return jsonify([c.to_dict() for c in feedbacks]), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@feedback_bp.route('/feedbacks_procedure', methods=['POST'])
def create_feedback_with_procedure():
    try:
        data = request.get_json()

        if not data or not all(key in data for key in ['comment', 'rating', 'driver_id']):
            return jsonify({'error': 'Invalid input data'}), 400

        service.create_feedback_with_procedure(data)
        return jsonify({'message': 'Feedback created successfully'}), 201

    except Exception as _:
        return jsonify({'error': 'bad request'}), 400


@feedback_bp.route('/feedbacks/random-tables', methods=['POST'])
def create_random_feedback_tables():
    """Створює нові таблиці із випадковими даними та перевіряє їх."""
    try:
        _ = service.create_and_validate_tables()
        return jsonify({'message': 'Tables created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@feedback_bp.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    from App.project.extension import db
    from sqlalchemy import text
    try:
        sql = text("DELETE FROM Feedbacks WHERE id = :feedback_id")
        db.session.execute(sql, {'feedback_id': feedback_id})
        db.session.commit()

        return jsonify({'message': f'Feedback with id {feedback_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': "You cant delete feedbacks"}), 500


