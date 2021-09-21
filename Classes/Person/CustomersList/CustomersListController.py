from Classes.Person.CustomersList.CustomersList import CustomersList


class CustomersListController:
    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(CustomersListController, self).__init__()
        self.model = CustomersList()
        # self.model = CustomersList(path)  # FOR TESTS

    def create_customer(self, name, surname, mail, password, date_of_birth, place_of_birth, phone_number, address, job,
                        payment_method, credit_card_number, permissions, valid_through, ccv, iban):
        return self.model.create_customer(name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                                          address, job, payment_method, credit_card_number, permissions, valid_through, ccv,
                                          iban)

    def get_customers_list(self):
        return self.model.get_customers_list()

    def get_customer_by_index(self, index):
        return self.model.get_customer_by_index(index)

    def get_customer_by_id(self, id_person):
        return self.model.get_customer_by_id(id_person)

    def update_customer_by_index(self, index, id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                 phone_number, address, job, payment_method, credit_card_number, permissions,
                                 valid_through, ccv, iban):
        return self.model.update_customer_by_index(index, id_person, name, surname, mail, password, date_of_birth,
                                                   place_of_birth, phone_number, address, job, payment_method,
                                                   credit_card_number, permissions, valid_through, ccv, iban)

    def update_customer_by_id(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                              phone_number, address, job, payment_method, credit_card_number, permissions,
                              valid_through, ccv, iban):
        return self.model.update_customer_by_id(id_person, name, surname, mail, password, date_of_birth,
                                                place_of_birth, phone_number, address, job, payment_method,
                                                credit_card_number, permissions, valid_through, ccv, iban)
