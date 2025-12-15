from App.project.auth.dao.shift_dao import ShiftDAO

class ShiftService:
    def __init__(self):
        self.dao = ShiftDAO()

    def get_all_shifts(self):
        return self.dao.get_all_shifts()

    def get_shift_by_id(self, shift_id):
        return self.dao.get_shift_by_id(shift_id)

    def create_shift(self, data):
        return self.dao.create_shift(data)

    def update_shift(self, shift_id, data):
        return self.dao.update_shift(shift_id, data)

    def delete_shift(self, shift_id):
        return self.dao.delete_shift(shift_id)
