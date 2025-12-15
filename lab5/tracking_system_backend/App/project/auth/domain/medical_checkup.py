from App.project.extension import db

class MedicalCheckup(db.Model):
    __tablename__ = 'medical_checkup'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    health_status = db.Column(db.String(200))
    blood_pressure = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'date': str(self.date),
            'health_status': self.health_status,
            'blood_pressure': self.blood_pressure,
            'heart_rate': self.heart_rate,
            'Driver_id': self.driver_id
        }
