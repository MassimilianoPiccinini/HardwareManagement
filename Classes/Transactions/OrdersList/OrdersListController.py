from Classes.Transactions.OrdersList.OrdersList import OrdersList


class OrdersListController:
    def __init__(self):
        super(OrdersListController, self).__init__()
        self.model = OrdersList()

    def create_order(self, date, quantity, id_product, id_supplier):
        return self.model.create_order(date, quantity, id_product, id_supplier)

    def get_orders_list(self):
        return self.model.get_orders_list()

    def get_order_by_index(self, index):
        return self.model.get_order_by_index(index)

    def delete_order_by_index(self, index):
        return self.model.delete_order_by_index(index)

    def update_order_by_index(self, index, id_transaction, date, quantity, id_product, id_supplier):
        return self.model.update_order_by_index(index, id_transaction, date, quantity, id_product, id_supplier)
