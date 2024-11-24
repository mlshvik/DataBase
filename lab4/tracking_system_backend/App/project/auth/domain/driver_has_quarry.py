from App.project.extension import db

class DriverHasQuarry(db.Model):
    __tablename__ = 'driver_has_quarry'

    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), primary_key=True)
    quarry_id = db.Column(db.Integer, db.ForeignKey('quarry.id'), primary_key=True)

    def to_dict(self):
        return {
            'Driver_id': self.driver_id,
            'Quarry_id': self.quarry_id
        }
