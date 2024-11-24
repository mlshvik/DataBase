from App.project.extension import db

class DriverAssignment(db.Model):
    __tablename__ = 'driver_assignment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'Driver_id': self.driver_id,
            'Vehicle_id': self.vehicle_id
        }
