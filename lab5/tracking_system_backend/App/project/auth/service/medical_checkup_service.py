from App.project.auth.dao.medical_checkup_dao import MedicalCheckupDAO

class MedicalCheckupService:
    def __init__(self):
        self.dao = MedicalCheckupDAO()

    def get_all_checkups(self):
        return self.dao.get_all_checkups()

    def get_checkup_by_id(self, checkup_id):
        return self.dao.get_checkup_by_id(checkup_id)

    def create_checkup(self, data):
        return self.dao.create_checkup(data)

    def update_checkup(self, checkup_id, data):
        return self.dao.update_checkup(checkup_id, data)

    def delete_checkup(self, checkup_id):
        return self.dao.delete_checkup(checkup_id)
