from App.project.extension import db
from App.project.auth.domain.maintenance import Maintenance

class MaintenanceDAO:
    def get_all_maintenance_records(self):
        return Maintenance.query.all()

    def get_maintenance_record_by_id(self, maintenance_id):
        return Maintenance.query.get(maintenance_id)

    def create_maintenance_record(self, data):
        new_maintenance_record = Maintenance(
            date=data['date'],
            description=data['description'],
            status=data['status'],
            vehicle_id=data['Vehicle_id']
        )
        db.session.add(new_maintenance_record)
        db.session.commit()
        return new_maintenance_record

    def update_maintenance_record(self, maintenance_id, data):
        maintenance_record = Maintenance.query.get(maintenance_id)
        if maintenance_record:
            maintenance_record.date = data.get('date', maintenance_record.date)
            maintenance_record.description = data.get('description', maintenance_record.description)
            maintenance_record.status = data.get('status', maintenance_record.status)
            maintenance_record.vehicle_id = data.get('Vehicle_id', maintenance_record.vehicle_id)
            db.session.commit()
            return maintenance_record
        return None

    def delete_maintenance_record(self, maintenance_id):
        maintenance_record = Maintenance.query.get(maintenance_id)
        if maintenance_record:
            db.session.delete(maintenance_record)
            db.session.commit()
            return True
        return False
