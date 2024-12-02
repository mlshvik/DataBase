from App.project.auth.domain.quarry import Quarry
from App.project.extension import db

from sqlalchemy import text


class QuarryDAO:
    def get_all_quarries(self):
        return Quarry.query.all()

    def get_quarry_by_id(self, quarry_id):
        return Quarry.query.get(quarry_id)

    def create_quarry(self, data):
        new_quarry = Quarry(
            name=data['name'],
            location=data['location'],
            operation_hours=data['operation_hours'],
            company_id=data['Company_id']
        )
        db.session.add(new_quarry)
        db.session.commit()
        return new_quarry

    def update_quarry(self, quarry_id, data):
        quarry = Quarry.query.get(quarry_id)
        if quarry:
            quarry.name = data.get('name', quarry.name)
            quarry.location = data.get('location', quarry.location)
            quarry.operation_hours = data.get('operation_hours', quarry.operation_hours)
            quarry.company_id = data.get('Company_id', quarry.company_id)
            db.session.commit()
            return quarry
        return None

    def delete_quarry(self, quarry_id):
        quarry = Quarry.query.get(quarry_id)
        if quarry:
            db.session.delete(quarry)
            db.session.commit()
            return True
        return False

    def insert_dummy_quarries(self):
        """Викликає збережену процедуру insert_dummy_quarries."""
        try:
            sql = text("CALL insert_dummy_quarries()")
            db.session.execute(sql)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
