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

    def create_connection(self, data):
        driver_name = data.get('driver_name')
        quarry_name = data.get('quarry_name')

        if not driver_name or not quarry_name:
            raise ValueError('Both driver_name and quarry_name are required')

        self.dao.insert_connection(driver_name, quarry_name)
