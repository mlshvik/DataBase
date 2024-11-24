from App.project.extension import db
from App.project.auth.domain.driver import Driver

class DriverDAO:
    def get_all_drivers(self):
        return Driver.query.all()

    def get_driver_by_id(self, driver_id):
        return Driver.query.get(driver_id)

    def create_driver(self, data):
        new_driver = Driver(
            name=data['name'],
            license_number=data['license_number'],
            experience_years=data['experience_years'],
            company_id=data['Company_id']
        )
        db.session.add(new_driver)
        db.session.commit()
        return new_driver

    def update_driver(self, driver_id, data):
        driver = Driver.query.get(driver_id)
        if driver:
            driver.name = data.get('name', driver.name)
            driver.license_number = data.get('license_number', driver.license_number)
            driver.experience_years = data.get('experience_years', driver.experience_years)
            driver.company_id = data.get('Company_id', driver.company_id)
            db.session.commit()
            return driver
        return None

    def delete_driver(self, driver_id):
        driver = Driver.query.get(driver_id)
        if driver:
            db.session.delete(driver)
            db.session.commit()
            return True
        return False
