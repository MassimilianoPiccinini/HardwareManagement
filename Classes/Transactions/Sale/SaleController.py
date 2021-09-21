from Classes.Transactions.TransactionController import TransactionController


class SaleController(TransactionController):
    def __init__(self, sale):
        TransactionController.__init__(self, sale)
        self.model = sale

    def get_id_client(self):
        return self.model.id_client

    def set_id_client(self, id_client):
        self.model.id_supplier = id_client
