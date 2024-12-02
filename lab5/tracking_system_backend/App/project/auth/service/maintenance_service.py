from App.project.auth.dao.maintenance_dao import MaintenanceDAO

class MaintenanceService:
    def __init__(self):
        self.dao = MaintenanceDAO()

    def get_all_maintenance_records(self):
        return self.dao.get_all_maintenance_records()

    def get_maintenance_record_by_id(self, maintenance_id):
        return self.dao.get_maintenance_record_by_id(maintenance_id)

    def create_maintenance_record(self, data):
        return self.dao.create_maintenance_record(data)

    def update_maintenance_record(self, maintenance_id, data):
        return self.dao.update_maintenance_record(maintenance_id, data)

    def delete_maintenance_record(self, maintenance_id):
        return self.dao.delete_maintenance_record(maintenance_id)
