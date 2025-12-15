from App.project.extension import db
from sqlalchemy import text
from App.project.auth.domain.feedback import Feedback


class FeedbackDAO:
    def get_all(self):
        return Feedback.query.all()

    def create(self, feedback):
        """Додаю і зразу в таблчику і зразу виводжу її дані"""
        db.session.add(feedback)
        db.session.commit()
        return self.get_all()

    def insert_feedback_with_procedure(self, feedback_date, comment, rating, driver_id):
        """Викликає збережену процедуру insert_feedback для додавання запису."""
        try:
            sql = text("""
                CALL insert_feedback(:feedback_date, :comment, :rating, :driver_id)
            """)
            db.session.execute(
                sql,
                {
                    'feedback_date': feedback_date,
                    'comment': comment,
                    'rating': rating,
                    'driver_id': driver_id
                }
            )
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def create_random_feedback_tables(self):
        """Викликає процедуру create_random_feedback_tables і повертає створені таблиці."""
        try:
            sql = text("CALL create_random_feedback_tables()")
            db.session.execute(sql)

            sql_get_tables = text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_name LIKE 'RandomFeedbackTable%' 
                ORDER BY create_time DESC 
                LIMIT 2
            """)
            result = db.session.execute(sql_get_tables).fetchall()

            db.session.commit()
            return [row[0] for row in result]
        except Exception as e:
            db.session.rollback()
            raise e
