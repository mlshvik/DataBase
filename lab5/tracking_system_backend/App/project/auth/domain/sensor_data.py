from App.project.extension import db

class SensorData(db.Model):
    __tablename__ = 'sensor_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.Time)
    location = db.Column(db.String(45))
    speed = db.Column(db.Integer)
    driver_health_status = db.Column(db.String(45))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': str(self.timestamp),
            'location': self.location,
            'speed': self.speed,
            'driver_health_status': self.driver_health_status,
            'Vehicle_id': self.vehicle_id
        }
