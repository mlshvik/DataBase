from App.project.auth.dao.vehicle_transfer_dao import VehicleTransferDAO
class VehicleTransferService:
    def __init__(self):
        self.dao = VehicleTransferDAO()

    def get_all_transfers(self):
        return self.dao.get_all_transfers()

    def get_transfer_by_id(self, transfer_id):
        return self.dao.get_transfer_by_id(transfer_id)

    def create_transfer(self, data):
        return self.dao.create_transfer(data)

    def update_transfer(self, transfer_id, data):
        return self.dao.update_transfer(transfer_id, data)

    def delete_transfer(self, transfer_id):
        return self.dao.delete_transfer(transfer_id)
