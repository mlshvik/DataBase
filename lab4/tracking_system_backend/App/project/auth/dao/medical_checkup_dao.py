from App.project.extension import db
from App.project.auth.domain.medical_checkup import MedicalCheckup

class MedicalCheckupDAO:
    def get_all_checkups(self):
        return MedicalCheckup.query.all()

    def get_checkup_by_id(self, checkup_id):
        return MedicalCheckup.query.get(checkup_id)

    def create_checkup(self, data):
        new_checkup = MedicalCheckup(
            date=data['date'],
            health_status=data['health_status'],
            blood_pressure=data['blood_pressure'],
            heart_rate=data['heart_rate'],
            driver_id=data['Driver_id']
        )
        db.session.add(new_checkup)
        db.session.commit()
        return new_checkup

    def update_checkup(self, checkup_id, data):
        checkup = MedicalCheckup.query.get(checkup_id)
        if checkup:
            checkup.date = data.get('date', checkup.date)
            checkup.health_status = data.get('health_status', checkup.health_status)
            checkup.blood_pressure = data.get('blood_pressure', checkup.blood_pressure)
            checkup.heart_rate = data.get('heart_rate', checkup.heart_rate)
            checkup.driver_id = data.get('Driver_id', checkup.driver_id)
            db.session.commit()
            return checkup
        return None

    def delete_checkup(self, checkup_id):
        checkup = MedicalCheckup.query.get(checkup_id)
        if checkup:
            db.session.delete(checkup)
            db.session.commit()
            return True
        return False
