from App.project.auth.dao.quarry_dao import QuarryDAO

class QuarryService:
    def __init__(self):
        self.dao = QuarryDAO()

    def get_all_quarries(self):
        return self.dao.get_all_quarries()

    def get_quarry_by_id(self, quarry_id):
        return self.dao.get_quarry_by_id(quarry_id)

    def create_quarry(self, data):
        return self.dao.create_quarry(data)

    def update_quarry(self, quarry_id, data):
        return self.dao.update_quarry(quarry_id, data)

    def delete_quarry(self, quarry_id):
        return self.dao.delete_quarry(quarry_id)
