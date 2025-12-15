from App.project.extension import db
from App.project.auth.domain.driver_assignment import DriverAssignment

class DriverAssignmentDAO:
    def get_all_assignments(self):
        return DriverAssignment.query.all()

    def get_assignment_by_id(self, assignment_id):
        return DriverAssignment.query.get(assignment_id)

    def create_assignment(self, data):
        new_assignment = DriverAssignment(
            start_date=data['start_date'],
            end_date=data['end_date'],
            driver_id=data['Driver_id'],
            vehicle_id=data['Vehicle_id']
        )
        db.session.add(new_assignment)
        db.session.commit()
        return new_assignment

    def update_assignment(self, assignment_id, data):
        assignment = DriverAssignment.query.get(assignment_id)
        if assignment:
            assignment.start_date = data.get('start_date', assignment.start_date)
            assignment.end_date = data.get('end_date', assignment.end_date)
            assignment.driver_id = data.get('Driver_id', assignment.driver_id)
            assignment.vehicle_id = data.get('Vehicle_id', assignment.vehicle_id)
            db.session.commit()
            return assignment
        return None

    def delete_assignment(self, assignment_id):
        assignment = DriverAssignment.query.get(assignment_id)
        if assignment:
            db.session.delete(assignment)
            db.session.commit()
            return True
        return False
