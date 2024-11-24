import os
import yaml
from flask import Flask
from App.project.extension import db
from App.project.auth.controller.company_controller import company_bp
from App.project.auth.controller.vehicle_controller import vehicle_bp
from App.project.auth.controller.quarry_controller import quarry_bp
from App.project.auth.controller.driver_controller import driver_bp
from App.project.auth.controller.sensor_data_controller import sensor_data_bp
from App.project.auth.controller.maintenance_controller import maintenance_bp
from App.project.auth.controller.shift_controller import shift_bp
from App.project.auth.controller.medical_checkup_controller import medical_checkup_bp
from App.project.auth.controller.vehicle_transfer_controller import vehicle_transfer_bp
from App.project.auth.controller.driver_assignment_controller import driver_assignment_bp
from App.project.auth.controller.driver_has_quarry_controller import driver_has_quarry_bp
app = Flask(__name__)


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(base_dir, "config", "app.yml")

#
with open(config_path) as f:
    config = yaml.safe_load(f)

db_config = config['database']
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


app.register_blueprint(company_bp, url_prefix='/api')
app.register_blueprint(quarry_bp, url_prefix='/api')
app.register_blueprint(vehicle_bp, url_prefix='/api')
app.register_blueprint(driver_bp, url_prefix='/api')
app.register_blueprint(sensor_data_bp, url_prefix='/api')
app.register_blueprint(maintenance_bp, url_prefix='/api')
app.register_blueprint(shift_bp, url_prefix='/api')
app.register_blueprint(medical_checkup_bp, url_prefix='/api')
app.register_blueprint(vehicle_transfer_bp, url_prefix='/api')
app.register_blueprint(driver_assignment_bp, url_prefix='/api')
app.register_blueprint(driver_has_quarry_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
