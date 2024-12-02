from App.project.extension import db
from App.project.auth.domain.company import Company


class CompanyDAO:
    def get_all(self):
        return Company.query.all()

    def get_by_id(self, company_id):
        return Company.query.get(company_id)

    def create(self, company):
        db.session.add(company)
        db.session.commit()
        return company

    def update(self, company):
        db.session.commit()
        return company

    def delete(self, company):
        db.session.delete(company)
        db.session.commit()
