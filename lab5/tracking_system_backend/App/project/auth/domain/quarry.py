from App.project.extension import db

class Quarry(db.Model):
    __tablename__ = 'quarry'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    location = db.Column(db.String(45))
    operation_hours = db.Column(db.Time)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'operation_hours': str(self.operation_hours),
            'Company_id': self.company_id
        }
