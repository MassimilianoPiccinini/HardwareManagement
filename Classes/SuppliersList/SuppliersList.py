import json
import uuid

from Classes.Supplier.Supplier import Supplier


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


class SuppliersList:

    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(SuppliersList, self).__init__()
        self.path = "Classes/suppliers.txt"
        # self.path = path  # FOR TESTS
        self.suppliers_list = self.get_suppliers_list()

    def get_suppliers_list(self):
        suppliers_array = []
        with open(self.path, 'r') as f:
            for supplier in json.load(f):
                supplier = Supplier(supplier["id"],
                                    supplier["name"],
                                    supplier["description"],
                                    supplier["mail"],
                                    supplier["phone_number"],
                                    supplier["address"])
                suppliers_array.append(supplier)
        return suppliers_array

    def get_supplier_by_id(self, id_supplier):
        for supplier in self.suppliers_list:
            if supplier.id_supplier == id_supplier:
                return supplier
        else:
            return None
