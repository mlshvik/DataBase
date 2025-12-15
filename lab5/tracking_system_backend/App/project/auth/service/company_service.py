from  App.project.auth.dao.company_dao import CompanyDAO
from  App.project.auth.domain.company import Company

class CompanyService:
    def __init__(self):
        self.dao = CompanyDAO()

    def get_all_companies(self):
        return self.dao.get_all()

    def get_company_by_id(self, company_id):
        return self.dao.get_by_id(company_id)

    def create_company(self, data):
        company = Company(name=data['name'], address=data['address'], contact_info=data['contact_info'])
        return self.dao.create(company)

    def update_company(self, company_id, data):
        company = self.dao.get_by_id(company_id)
        if company:
            company.name = data['name']
            company.address = data['address']
            company.contact_info = data['contact_info']
            return self.dao.update(company)
        return None

    def delete_company(self, company_id):
        company = self.dao.get_by_id(company_id)
        if company:
            self.dao.delete(company)
            return True
        return False
