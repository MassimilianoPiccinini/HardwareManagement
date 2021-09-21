import json
import uuid

from Classes.Person.Customer.Customer import Customer


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


class CustomersList:
    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(CustomersList, self).__init__()
        self.path = "Classes/Person/users.txt"
        # self.path = path  # FOR TESTS
        self.customers_list = self.get_customers_list()

    def is_person_registered_id(self, id_person):
        with open(self.path, 'r') as f:
            for person in json.load(f):
                if person['id'] == id_person:
                    return True
            f.close()
            return False

    def is_person_registered_mail(self, mail):
        with open(self.path, 'r') as f:
            for person in json.load(f):
                if person['mail'] == mail:
                    return True
            f.close()
            return False

    def create_customer(self, name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                        address, job, payment_method, credit_card_number, permissions, valid_trough, ccv, iban):
        if not self.is_person_registered_mail(mail):
            with open(self.path, 'r') as fr:
                customers_array = json.load(fr)
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
                    'payment_method': payment_method,
                    'credit_card_number': credit_card_number,
                    'permissions': permissions,
                    'valid_trough': valid_trough,
                    'ccv': ccv,
                    'iban': iban,
                    'job': 0
                }
                customers_array.append(new_user)

                j = json.dumps(customers_array)
                with open(self.path, 'w') as fw:
                    fw.write(j)
                    fw.close()
                    customer = Customer(id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                        phone_number, address, job, payment_method, credit_card_number, permissions,
                                        valid_trough, ccv, iban)
                    self.customers_list.append(customer)
                    return True

        else:
            return False

    def get_customers_list(self):
        customers_array = []
        fr = open(self.path, 'r')
        for person in json.load(fr):
            if person['job'] == 0:
                customer = Customer(person['id'],
                                    person['name'],
                                    person['surname'],
                                    person['mail'],
                                    person['password'],
                                    person['date_of_birth'],
                                    person['place_of_birth'],
                                    person['phone_number'],
                                    person['address'],
                                    0,
                                    person['payment_method'],
                                    person['credit_card_number'],
                                    person['permissions'],
                                    person['valid_trough'],
                                    person['ccv'],
                                    person['iban'])
                customers_array.append(customer)
        fr.close()
        return customers_array

    def get_customer_by_index(self, index):
        if 0 <= index < len(self.customers_list):
            return self.customers_list[index]
        else:
            return None

    def get_customer_by_id(self, id_customer):
        for customer in self.get_customers_list():
            if customer.id_person == id_customer:
                return customer

    def update_customer_by_index(self, index, id_person, name, surname, mail, password, date_of_birth,
                                 place_of_birth, phone_number, address, job, payment_method, credit_card_number,
                                 permissions, valid_trough, ccv, iban):
        if 0 <= index < len(self.customers_list):
            if self.is_person_registered_id(id_person):
                with open(self.path, 'r') as f:
                    customers_array = json.load(f)
                    customer_index = 0
                    for person in customers_array:
                        if person['id'] == id_person:
                            person['name'] = name
                            person['surname'] = surname
                            person['mail'] = mail
                            person['password'] = password
                            person['date_of_birth'] = date_of_birth
                            person['place_of_birth'] = place_of_birth
                            person['phone_number'] = phone_number
                            person['address'] = address
                            person['payment_method'] = payment_method
                            person['credit_card_number'] = credit_card_number
                            person['permissions'] = permissions
                            person['valid_trough'] = valid_trough
                            person['ccv'] = ccv
                            person['iban'] = iban
                            customer = Customer(id_person, name, surname, mail, password, date_of_birth,
                                                place_of_birth,
                                                phone_number, address, job, payment_method, credit_card_number,
                                                permissions, valid_trough, ccv, iban)
                            customers_array[customer_index] = {
                                'id': id_person,
                                'name': name,
                                'surname': surname,
                                'mail': mail,
                                'password': password,
                                'date_of_birth': date_of_birth,
                                'place_of_birth': place_of_birth,
                                'phone_number': phone_number,
                                'address': address,
                                'payment_method': payment_method,
                                'credit_card_number': credit_card_number,
                                'permissions': permissions,
                                'valid_trough': valid_trough,
                                'ccv': ccv,
                                'iban': iban,
                                'job': 0
                            }
                            self.customers_list[index] = customer
                            break
                        customer_index = customer_index + 1

                    j = json.dumps(customers_array)
                    with open(self.path, 'w') as fw:
                        fw.write(j)
                        fw.close()
                f.close()
                return True
            return False
        return False

    def update_customer_by_id(self, id_person, name, surname, mail, password, date_of_birth,
                              place_of_birth, phone_number, address, job, payment_method, credit_card_number,
                              permissions, valid_trough, ccv, iban):
        if self.is_person_registered_id(id_person):
            with open(self.path, 'r') as f:
                customers_array = json.load(f)
                index = 0
                for person in customers_array:
                    if person['id'] == id_person and person['job'] == 0:
                        self.update_customer_by_index(index, id_person, name, surname, mail, password, date_of_birth,
                                                      place_of_birth, phone_number, address, job, payment_method,
                                                      credit_card_number, permissions, valid_trough, ccv, iban)
                    else:
                        index += 1
