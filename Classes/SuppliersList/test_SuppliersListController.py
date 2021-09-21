from unittest import TestCase

from Classes.Supplier.Supplier import Supplier
from Classes.SuppliersList.SuppliersListController import SuppliersListController

import os


class TestSuppliersListController(TestCase):
    def test_get_suppliers_list(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SuppliersListController(classes_path + '/suppliers.txt')
        suppliers = controller.get_suppliers_list()
        supplier = suppliers[0]
        my_supplier = Supplier("1234567", "Hexanon", "Best app ever", "hexanon@gmail.com", "3312373893",
                               "Via Altotting, 37")
        self.assertEqual(supplier.name, my_supplier.name)
        self.assertEqual(supplier.mail, my_supplier.mail)
        self.assertEqual(supplier.address, my_supplier.address)

    def test_get_supplier_by_id(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SuppliersListController(classes_path + '/suppliers.txt')
        supplier = controller.get_supplier_by_id("1234567")
        my_supplier = Supplier("1234567", "Hexanon", "Best app ever", "hexanon@gmail.com", "3312373893",
                               "Via Altotting, 37")
        self.assertEqual(supplier.name, my_supplier.name)
        self.assertEqual(supplier.mail, my_supplier.mail)
        self.assertEqual(supplier.address, my_supplier.address)
