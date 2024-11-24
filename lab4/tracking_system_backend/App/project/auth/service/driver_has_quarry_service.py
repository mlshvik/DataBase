from App.project.auth.dao.driver_has_quarry_dao import DriverHasQuarryDAO

class DriverHasQuarryService:
    def __init__(self):
        self.dao = DriverHasQuarryDAO()

    def get_all_assignments(self):
        return self.dao.get_all_assignments()

    def add_assignment(self, data):
        return self.dao.add_assignment(data)

    def delete_assignment(self, driver_id, quarry_id):
        return self.dao.delete_assignment(driver_id, quarry_id)
