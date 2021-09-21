from Classes.ProductsList.ProductsList import ProductsList


class ProductsListController:
    # def __init__(self, path): # FOR TESTS
    def __init__(self):
        super(ProductsListController, self).__init__()
        self.model = ProductsList()
        # self.model = ProductsList(path)  # FOR TESTS

    def get_products_list(self):
        return self.model.get_products_list()

    def get_product_by_index(self, index):
        return self.model.get_product_by_index(index)

    def get_product_by_id(self, id_product):
        return self.model.get_product_by_id(id_product)

    def update_product_by_id(self, id_product, name, description, price, quantity, volume, weight):
        return self.model.update_product_by_id(id_product, name, description, price, quantity, volume, weight)

    def search_by_name(self, name):
        return self.model.search_by_name(name)
