from App.project.extension import db
from App.project.auth.domain.shift import Shift

class ShiftDAO:
    def get_all_shifts(self):
        return Shift.query.all()

    def get_shift_by_id(self, shift_id):
        return Shift.query.get(shift_id)

    def create_shift(self, data):
        new_shift = Shift(
            date=data['date'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            vehicle_id=data['Vehicle_id'],
            driver_id=data['Driver_id']
        )
        db.session.add(new_shift)
        db.session.commit()
        return new_shift

    def update_shift(self, shift_id, data):
        shift = Shift.query.get(shift_id)
        if shift:
            shift.date = data.get('date', shift.date)
            shift.start_time = data.get('start_time', shift.start_time)
            shift.end_time = data.get('end_time', shift.end_time)
            shift.vehicle_id = data.get('Vehicle_id', shift.vehicle_id)
            shift.driver_id = data.get('Driver_id', shift.driver_id)
            db.session.commit()
            return shift
        return None

    def delete_shift(self, shift_id):
        shift = Shift.query.get(shift_id)
        if shift:
            db.session.delete(shift)
            db.session.commit()
            return True
        return False
