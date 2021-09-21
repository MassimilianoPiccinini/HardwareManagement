from unittest import TestCase

from Classes.Person.Customer.Customer import Customer
from Classes.Person.CustomersList.CustomersListController import CustomersListController

import os

# TODO: in order to execute tests, we must change the path directory manually, because the test path is different from
# TODO: the file path that is called. So the changes must be done both in controller and in model, uncommenting rows
# TODO: with the comment : FOR TESTS


class TestCustomersListController(TestCase):

    # TODO: delete real Mario Rossi before testing
    def test_create_customer(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        person_path = os.path.abspath(os.path.dirname(prev_path))
        controller = CustomersListController(person_path + '/users.txt')
        success = controller.create_customer('Mario', 'Rossi', 'mariorossi@gmail.com', 'my_pass', '02/06/1946', 'Castellabbate',
                                   '3331234567', 'via Brombeis', 0, 0, '', 0, '', '', '')
        self.assertTrue(success)

    def test_get_customer_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        person_path = os.path.abspath(os.path.dirname(prev_path))
        controller = CustomersListController(person_path + '/users.txt')
        customer = controller.get_customer_by_index(0)
        my_customer = Customer('XJ410K73J532', 'Max', 'Piccinini', 'massimilianopiccinini.8@gmail.com', 'ciao', '13/07/2000', 'Recanati', '3312373893', 'Via Altotting, 37', 0, 0, '123456', 0, '13/07', '123', '')
        self.assertEqual(customer.name, my_customer.name)
        self.assertEqual(customer.mail, my_customer.mail)
        self.assertEqual(customer.credit_card_number, my_customer.credit_card_number)
        self.assertEqual(customer.iban, my_customer.iban)

    def test_update_customer_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        person_path = os.path.abspath(os.path.dirname(prev_path))
        controller = CustomersListController(person_path + '/users.txt')
        success = controller.update_customer_by_index(1, 'XJ410K73J532', 'Max', 'Piccinini', 'massimilianopiccinini.8@gmail.com', 'ciao',
                               '13/07/2000', 'Recanati', '3312373893', 'Via Altotting, 37', 0, 0, '123456', 0, '13/07',
                               '123', '')
        self.assertTrue(success)
