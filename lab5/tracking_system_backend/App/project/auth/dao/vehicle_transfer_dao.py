from App.project.auth.domain.vehicle_transfer import VehicleTransfer
from App.project.extension import db

class VehicleTransferDAO:
    def get_all_transfers(self):
        return VehicleTransfer.query.all()

    def get_transfer_by_id(self, transfer_id):
        return VehicleTransfer.query.get(transfer_id)

    def create_transfer(self, data):
        new_transfer = VehicleTransfer(
            transfer_date=data['transfer_date'],
            vehicle_id=data['Vehicle_id'],
            quarry_id=data['Quarry_id']
        )
        db.session.add(new_transfer)
        db.session.commit()
        return new_transfer

    def update_transfer(self, transfer_id, data):
        transfer = VehicleTransfer.query.get(transfer_id)
        if transfer:
            transfer.transfer_date = data.get('transfer_date', transfer.transfer_date)
            transfer.vehicle_id = data.get('Vehicle_id', transfer.vehicle_id)
            transfer.quarry_id = data.get('Quarry_id', transfer.quarry_id)
            db.session.commit()
            return transfer
        return None

    def delete_transfer(self, transfer_id):
        transfer = VehicleTransfer.query.get(transfer_id)
        if transfer:
            db.session.delete(transfer)
            db.session.commit()
            return True
        return False
