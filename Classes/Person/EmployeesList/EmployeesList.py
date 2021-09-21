import json
import uuid

from Classes.Person.Employee.Employee import Employee


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


def is_person_registered(id_person):
    with open("Classes/Person/users.txt", 'r') as f:
        for person in json.load(f):
            if person['id'] == id_person:
                return True
        f.close()
        return False


class EmployeesList:
    def __init__(self):
        super(EmployeesList, self).__init__()
        self.employees_list = self.get_employees_list()

    def create_employee(self, name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                        address, job, role, salary, permissions, hire_date):
        with open("Classes/Person/users.txt", 'r') as fr:
            employees_array = json.load(fr)
            fr.close()
            id_person = generate_id()
            new_user = {
                'id': id_person,
                'name': name,
                'surname': surname,
                'mail': mail,
                'password': password,
                'date_of_birth': date_of_birth,
                'place_of_birth': place_of_birth,
                'phone_number': phone_number,
                'address': address,
                'role': role,
                'salary': salary,
                'permissions': permissions,
                'hire_date': hire_date,
                'job': 1
            }
            employees_array.append(new_user)

            j = json.dumps(employees_array)
            with open("Classes/Person/users.txt", 'w') as fw:
                fw.write(j)
                fw.close()
                employee = Employee(id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                    phone_number, address, job, role, salary, permissions, hire_date)
                self.employees_list.append(employee)
                return True

    def get_employees_list(self):
        employees_array = []
        for person in json.load(open("Classes/Person/users.txt", 'r')):
            if person['job'] == 1:
                employee = Employee(person['id'],
                                    person['name'],
                                    person['surname'],
                                    person['mail'],
                                    person['password'],
                                    person['date_of_birth'],
                                    person['place_of_birth'],
                                    person['phone_number'],
                                    person['address'],
                                    1,
                                    person['role'],
                                    person['salary'],
                                    person['permissions'],
                                    person['hire_date'])
                employees_array.append(employee)
        return employees_array

    def get_employee_by_index(self, index):
        if 0 <= index < len(self.employees_list):
            return self.employees_list[index]
        else:
            return None

    def delete_employee_by_index(self, index):
        if 0 <= index < len(self.employees_list):
            id_employee = self.employees_list[index].id_person
            if is_person_registered(id_employee):
                with open("Classes/Person/users.txt", 'r') as f:
                    employees_array = json.load(f)
                    for person in employees_array:
                        if person['id'] == id_employee:
                            employees_array.remove(person)
                            break
                    j = json.dumps(employees_array)
                    with open("Classes/Person/users.txt", 'w') as fw:
                        fw.write(j)
                        fw.close()
                del self.employees_list[index]
            return False
        return False

    def update_employee_by_index(self, index, id_person, name, surname, mail, password, date_of_birth,
                                 place_of_birth, phone_number, address, job, role, salary, permissions, hire_date):
        if 0 <= index < len(self.employees_list):
            if is_person_registered(id_person):
                with open("Classes/Person/users.txt", 'r') as f:
                    people_array = json.load(f)
                    employees_index = 0
                    for person in people_array:
                        if person['id'] == id_person:
                            person['name'] = name
                            person['surname'] = surname
                            person['mail'] = mail
                            person['password'] = password
                            person['date_of_birth'] = date_of_birth
                            person['place_of_birth'] = place_of_birth
                            person['phone_number'] = phone_number
                            person['address'] = address
                            person['role'] = role
                            person['salary'] = salary
                            person['permissions'] = permissions
                            person['hire_date'] = hire_date
                            employee = Employee(id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                                phone_number, address, job, role, salary, permissions, hire_date)
                            # TODO: change index
                            people_array[employees_index] = {
                                'id': id_person,
                                'name': name,
                                'surname': surname,
                                'mail': mail,
                                'password': password,
                                'date_of_birth': date_of_birth,
                                'place_of_birth': place_of_birth,
                                'phone_number': phone_number,
                                'address': address,
                                'role': role,
                                'salary': salary,
                                'permissions': permissions,
                                'hire_date': hire_date,
                                'job': 1
                            }
                            self.employees_list[index] = employee
                            break
                        employees_index = employees_index + 1

                    j = json.dumps(people_array)
                    with open("Classes/Person/users.txt", 'w') as fw:
                        fw.write(j)
                        fw.close()
                f.close()
                return True
            return False
        return False
