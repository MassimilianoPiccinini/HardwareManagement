class Transaction:
    def __init__(self, id_transaction, date, quantity, id_product):
        super(Transaction, self).__init__()
        self.id_transaction = id_transaction
        self.date = date
        self.quantity = quantity
        self.id_product = id_product
