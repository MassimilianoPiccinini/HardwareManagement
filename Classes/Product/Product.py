class Product:
    def __init__(self, id_product, name, description, price, quantity, volume, weight):
        super(Product, self).__init__()
        self.id_product = id_product
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.volume = volume
        self.weight = weight
