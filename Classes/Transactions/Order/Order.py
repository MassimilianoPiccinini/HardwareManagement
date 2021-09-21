from Classes.Transactions.Transaction import Transaction


class Order(Transaction):
    def __init__(self, id_transaction, date, quantity, id_product, id_supplier):
        Transaction.__init__(self, id_transaction, date, quantity, id_product)
        self.id_supplier = id_supplier
