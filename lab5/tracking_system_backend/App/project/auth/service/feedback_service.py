from datetime import datetime

from  App.project.auth.dao.feedback_dao import FeedbackDAO
from  App.project.auth.domain.feedback import Feedback
class FeedbackService:
    def __init__(self):
        self.dao = FeedbackDAO()

    def get_all_feedbacks(self):
        return self.dao.get_all()

    def create_and_get_all_feedbacks(self, feedback):
        feedback_obj = Feedback(
            feedback_date=feedback["feedback_date"],
            comment=feedback["comment"],
            rating=feedback["rating"],
            driver_id=feedback["driver_id"]
        )
        return self.dao.create(feedback_obj)

    def create_feedback_with_procedure(self, data):
        feedback_date = data.get('feedback_date', datetime.now().strftime('%Y-%m-%d'))
        comment = data['comment']
        rating = data['rating']
        driver_id = data['driver_id']

        self.dao.insert_feedback_with_procedure(feedback_date, comment, rating, driver_id)

    def create_and_validate_tables(self):
        """
        Викликає процедуру створення таблиць.
        Перевіряє, чи дані рівномірно розподілилися.
        У разі невдачі повторює спробу.
        """
        MAX_RETRIES = 3
        for attempt in range(MAX_RETRIES):
            tables = self.dao.create_random_feedback_tables()
            return tables
