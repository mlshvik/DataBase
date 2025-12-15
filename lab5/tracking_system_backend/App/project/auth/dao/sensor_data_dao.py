from App.project.extension import db
from App.project.auth.domain.sensor_data import SensorData

class SensorDataDAO:
    def get_all_sensor_data(self):
        return SensorData.query.all()

    def get_sensor_data_by_id(self, sensor_data_id):
        return SensorData.query.get(sensor_data_id)

    def create_sensor_data(self, data):
        new_sensor_data = SensorData(
            timestamp=data['timestamp'],
            location=data['location'],
            speed=data['speed'],
            driver_health_status=data['driver_health_status'],
            vehicle_id=data['Vehicle_id']
        )
        db.session.add(new_sensor_data)
        db.session.commit()
        return new_sensor_data

    def update_sensor_data(self, sensor_data_id, data):
        sensor_data = SensorData.query.get(sensor_data_id)
        if sensor_data:
            sensor_data.timestamp = data.get('timestamp', sensor_data.timestamp)
            sensor_data.location = data.get('location', sensor_data.location)
            sensor_data.speed = data.get('speed', sensor_data.speed)
            sensor_data.driver_health_status = data.get('driver_health_status', sensor_data.driver_health_status)
            sensor_data.vehicle_id = data.get('Vehicle_id', sensor_data.vehicle_id)
            db.session.commit()
            return sensor_data
        return None

    def delete_sensor_data(self, sensor_data_id):
        sensor_data = SensorData.query.get(sensor_data_id)
        if sensor_data:
            db.session.delete(sensor_data)
            db.session.commit()
            return True
        return False
