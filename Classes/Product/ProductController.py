class ProductController:
    def __init__(self, product):
        self.model = product

    def get_id_product(self):
        return self.model.id_product

    def set_id_product(self, id_product):
        self.model.id_product = id_product

    def get_name(self):
        return self.model.name

    def set_name(self, name):
        self.model.name = name

    def get_description(self):
        return self.model.description

    def set_description(self, description):
        self.model.description = description

    def get_price(self):
        return self.model.price

    def set_price(self, price):
        self.model.price = price

    def get_quantity(self):
        return self.model.quantity

    def set_quantity(self, quantity):
        self.model.quantity = quantity

    def get_volume(self):
        return self.model.volume

    def set_volume(self, volume):
        self.model.volume = volume

    def get_weight(self):
        return self.model.weight

    def set_weight(self, weight):
        self.model.weight = weight

