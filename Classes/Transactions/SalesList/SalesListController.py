from Classes.Transactions.SalesList.SalesList import SalesList


class SalesListController:
    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(SalesListController, self).__init__()
        self.model = SalesList()
        # self.model = SalesList(path)  # FOR TESTS

    def create_sale(self, date, quantity, id_product, id_client):
        return self.model.create_sale(date, quantity, id_product, id_client)

    def get_sales_list(self):
        return self.model.get_sales_list()

    def get_mine_sales_list(self, id_person):
        return self.model.get_mine_sales_list(id_person)

    def get_sale_by_index(self, index):
        return self.model.get_sale_by_index(index)

    def get_mine_sale_by_index(self, index, id_person):
        return self.model.get_mine_sale_by_index(index, id_person)

    def delete_mine_sale_by_index(self, index, id_person):
        return self.model.delete_mine_sale_by_index(index, id_person)

    def update_mine_sale_by_index(self, index, id_transaction, date, quantity, id_product, id_client, id_person):
        return self.model.update_sale_by_index(index, id_transaction, date, quantity, id_product, id_client, id_person)
