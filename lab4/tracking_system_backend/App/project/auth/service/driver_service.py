from App.project.auth.dao.driver_dao import DriverDAO

class DriverService:
    def __init__(self):
        self.dao = DriverDAO()

    def get_all_drivers(self):
        return self.dao.get_all_drivers()

    def get_driver_by_id(self, driver_id):
        return self.dao.get_driver_by_id(driver_id)

    def create_driver(self, data):
        return self.dao.create_driver(data)

    def update_driver(self, driver_id, data):
        return self.dao.update_driver(driver_id, data)

    def delete_driver(self, driver_id):
        return self.dao.delete_driver(driver_id)
