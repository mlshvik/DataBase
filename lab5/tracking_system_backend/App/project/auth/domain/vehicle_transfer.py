from App.project.extension import db

class VehicleTransfer(db.Model):
    __tablename__ = 'vehicle_transfer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transfer_date = db.Column(db.Date)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    quarry_id = db.Column(db.Integer, db.ForeignKey('quarry.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'transfer_date': str(self.transfer_date),
            'Vehicle_id': self.vehicle_id,
            'Quarry_id': self.quarry_id
        }
