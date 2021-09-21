import json
import uuid

from Classes.Product.Product import Product


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


class ProductsList:

    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(ProductsList, self).__init__()
        self.path = "Classes/storage.txt"
        # self.path = path  # FOR TESTS
        self.products_list = self.get_products_list()

    def is_product_in_storage(self, id_product):
        with open(self.path, 'r') as f:
            for product in json.load(f):
                if product['id'] == id_product:
                    return True
            f.close()
            return False

    def get_products_list(self):
        products_array = []
        with open(self.path, 'r') as f:
            for product in json.load(f):
                product = Product(product["id"],
                                  product["name"],
                                  product["description"],
                                  product["price"],
                                  product["quantity"],
                                  product["volume"],
                                  product["weight"])
                products_array.append(product)
        return products_array

    def get_product_by_index(self, index):
        if 0 <= index < len(self.products_list):
            return self.products_list[index]
        else:
            return None

    def get_product_by_id(self, id_product):
        for product in self.products_list:
            if product.id_product == id_product:
                return product

        return None

    def update_product_by_id(self, id_product, name, description, price, quantity, volume, weight):
        if self.is_product_in_storage(id_product):
            with open(self.path, 'r') as f:
                products_array = json.load(f)
                for product in products_array:
                    if product['id'] == id_product:
                        product['name'] = name
                        product['description'] = description
                        product['price'] = price
                        product['quantity'] = quantity
                        product['volume'] = volume
                        product['weight'] = weight
                        my_product = Product(id_product, name, description, price, quantity, volume, weight)
                        index = 0
                        for prod in products_array:
                            if prod['id'] == id_product:
                                break
                            index = index + 1

                        products_array[index] = {
                            'id': id_product,
                            'name': name,
                            'description': description,
                            'price': price,
                            'quantity': quantity,
                            'volume': volume,
                            'weight': weight
                        }
                        self.products_list[index] = my_product
                        break

                j = json.dumps(products_array)
                with open(self.path, 'w') as fw:
                    fw.write(j)
                    fw.close()
            f.close()
            return True
        return False

    def search_by_name(self, name):
        products_list = []
        for product in self.products_list:
            if name.strip().lower() in product.name.strip().lower():
                products_list.append(product)
        return products_list
