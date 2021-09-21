from Classes.Person.PersonController import PersonController


class EmployeeController(PersonController):
    def __init__(self, employee):
        PersonController.__init__(self, employee)
        self.model = employee

    def get_role(self):
        return self.model.role

    def set_role(self, role):
        self.model.role = role

    def get_salary(self):
        return self.model.salary

    def set_salary(self, salary):
        self.model.salary = salary

    def get_permissions(self):
        return self.model.permissions

    def set_permissions(self, permissions):
        self.model.permissions = permissions

    def get_id_supplier(self):
        return self.model.id_supplier

    def set_id_supplier(self, id_supplier):
        self.model.id_supplier = id_supplier

    def get_hire_date(self):
        return self.model.hire_date

    def set_hire_date(self, hire_date):
        self.model.hire_date = hire_date
