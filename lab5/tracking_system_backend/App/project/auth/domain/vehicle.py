from App.project.extension import db

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45))
    model = db.Column(db.String(10))
    capacity = db.Column(db.Integer)
    vehicle_numbers = db.Column(db.String(45))
    quarry_id = db.Column(db.Integer, db.ForeignKey('quarry.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'model': self.model,
            'capacity': self.capacity,
            'vehicle_numbers': self.vehicle_numbers,
            'Quarry_id': self.quarry_id
        }
