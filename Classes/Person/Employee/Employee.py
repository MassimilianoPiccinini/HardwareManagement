from Classes.Person.Person import Person


class Employee(Person):
    def __init__(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number, address,
                 job, role, salary, permissions, hire_date):
        Person.__init__(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                        address, job)
        self.role = role
        self.salary = salary
        self.permissions = permissions
        self.hire_date = hire_date
