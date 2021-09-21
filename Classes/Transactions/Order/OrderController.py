from Classes.Transactions.TransactionController import TransactionController


class OrderController(TransactionController):
    def __init__(self, order):
        TransactionController.__init__(self, order)
        self.model = order

    def get_id_supplier(self):
        return self.model.id_supplier

    def set_id_supplier(self, id_supplier):
        self.model.id_supplier = id_supplier
