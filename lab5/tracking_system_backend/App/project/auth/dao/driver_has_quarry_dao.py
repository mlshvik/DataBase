from App.project.extension import db
from sqlalchemy import text
from App.project.auth.domain.driver_has_quarry import DriverHasQuarry


class DriverHasQuarryDAO:
    def get_all_assignments(self):
        return DriverHasQuarry.query.all()

    def add_assignment(self, data):
        new_assignment = DriverHasQuarry(
            driver_id=data['Driver_id'],
            quarry_id=data['Quarry_id']
        )
        db.session.add(new_assignment)
        db.session.commit()
        return new_assignment

    def insert_connection(self, driver_name, quarry_name):
        try:
            sql = text("""
                CALL insert_driver_quarry_connection(:driver_name, :quarry_name)
            """)
            db.session.execute(
                sql,
                {'driver_name': driver_name, 'quarry_name': quarry_name}
            )
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_assignment(self, driver_id, quarry_id):
        assignment = DriverHasQuarry.query.get((driver_id, quarry_id))
        if assignment:
            db.session.delete(assignment)
            db.session.commit()
            return True
        return False
