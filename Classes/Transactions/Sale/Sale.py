from Classes.Transactions.Transaction import Transaction


class Sale(Transaction):
    def __init__(self, id_transaction, date, quantity, id_product, id_client):
        Transaction.__init__(self, id_transaction, date, quantity, id_product)
        self.id_client = id_client
