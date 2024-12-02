from App.project.extension import db


class Feedback(db.Model):
    __tablename__ = 'Feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    feedback_date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    driver_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'feedback_date': self.feedback_date.strftime('%Y-%m-%d') if self.feedback_date else None,
            'comment': self.comment,
            'rating': self.rating,
            'driver_id': self.driver_id,
        }


