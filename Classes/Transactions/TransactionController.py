class TransactionController:
    def __init__(self, transaction):
        self.model = transaction

    def get_id_transaction(self):
        return self.model.id_transaction

    def get_date(self):
        return self.model.date

    def get_quantity(self):
        return self.model.quantity

    def get_id_product(self):
        return self.model.id_product

    def set_id_transaction(self, id_transaction):
        self.model.id_transaction = id_transaction

    def set_date(self, date):
        self.model.date = date

    def set_quantity(self, quantity):
        self.model.quantity = quantity

    def set_id_product(self, id_product):
        self.model.id_product = id_product
