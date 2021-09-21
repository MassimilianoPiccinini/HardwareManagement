from Classes.Person.EmployeesList.EmployeesList import EmployeesList


class EmployeesListController:
    def __init__(self):
        super(EmployeesListController, self).__init__()
        self.model = EmployeesList()

    def create_employee(self, name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                        address, job, role, salary, permissions, hire_date):
        return self.model.create_employee(name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                                          address, job, role, salary, permissions, hire_date)

    def get_employees_list(self):
        return self.model.get_employees_list()

    def get_employee_by_index(self, index):
        return self.model.get_employee_by_index(index)

    def delete_employee_by_index(self, index):
        return self.model.delete_employee_by_index(index)

    def update_employee_by_index(self, index, id_person, name, surname, mail, password, date_of_birth,
                                 place_of_birth, phone_number, address, job, role, salary, permissions, hire_date):
        return self.model.update_employee_by_index(index, id_person, name, surname, mail, password, date_of_birth,
                                                   place_of_birth, phone_number, address, job, role, salary,
                                                   permissions, hire_date)
