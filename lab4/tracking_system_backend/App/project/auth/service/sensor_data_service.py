from App.project.auth.dao.sensor_data_dao import SensorDataDAO

class SensorDataService:
    def __init__(self):
        self.dao = SensorDataDAO()

    def get_all_sensor_data(self):
        return self.dao.get_all_sensor_data()

    def get_sensor_data_by_id(self, sensor_data_id):
        return self.dao.get_sensor_data_by_id(sensor_data_id)

    def create_sensor_data(self, data):
        return self.dao.create_sensor_data(data)

    def update_sensor_data(self, sensor_data_id, data):
        return self.dao.update_sensor_data(sensor_data_id, data)

    def delete_sensor_data(self, sensor_data_id):
        return self.dao.delete_sensor_data(sensor_data_id)
