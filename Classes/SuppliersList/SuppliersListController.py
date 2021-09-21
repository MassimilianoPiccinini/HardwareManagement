from Classes.SuppliersList.SuppliersList import SuppliersList


class SuppliersListController:

    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(SuppliersListController, self).__init__()
        self.model = SuppliersList()
        # self.model = SuppliersList(path)  # FOR TESTS

    def get_suppliers_list(self):
        return self.model.get_suppliers_list()

    def get_supplier_by_id(self, id_supplier):
        return self.model.get_supplier_by_id(id_supplier)
