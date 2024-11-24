from App.project.auth.dao.driver_assignment_dao import DriverAssignmentDAO

class DriverAssignmentService:
    def __init__(self):
        self.dao = DriverAssignmentDAO()

    def get_all_assignments(self):
        return self.dao.get_all_assignments()

    def get_assignment_by_id(self, assignment_id):
        return self.dao.get_assignment_by_id(assignment_id)

    def create_assignment(self, data):
        return self.dao.create_assignment(data)

    def update_assignment(self, assignment_id, data):
        return self.dao.update_assignment(assignment_id, data)

    def delete_assignment(self, assignment_id):
        return self.dao.delete_assignment(assignment_id)
