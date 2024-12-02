from App.project.extension import db

class Maintenance(db.Model):
    __tablename__ = 'maintenance'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'date': str(self.date),
            'description': self.description,
            'status': self.status,
            'Vehicle_id': self.vehicle_id
        }
