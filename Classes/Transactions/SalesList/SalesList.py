import json
import random
import uuid
import os  # FOR TESTS

from Classes.Transactions.Sale.Sale import Sale
from Classes.ProductsList.ProductsListController import ProductsListController


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


class SalesList:

    # def __init__(self, path):  # FOR TESTS
    def __init__(self):
        super(SalesList, self).__init__()
        self.path = "Classes/Transactions/transactions.txt"
        # self.path = path  # FOR TESTS
        self.sales_list = self.get_sales_list()

    def is_transaction_ended(self, id_transaction):
        with open(self.path, 'r') as f:
            for transaction in json.load(f):
                if transaction['id'] == id_transaction:
                    return True
            f.close()
            return False

    def create_sale(self, date, quantity, id_product, id_client):
        with open(self.path, 'r') as fr:
            transactions_array = json.load(fr)
            fr.close()
            id_transaction = generate_id()
            new_user = {
                'id': id_transaction,
                'date': date,
                'quantity': quantity,
                'id_product': id_product,
                'id_client': id_client,
                'is_selling': True
            }
            transactions_array.append(new_user)

            j = json.dumps(transactions_array)
            with open(self.path, 'w') as fw:
                fw.write(j)
                fw.close()
                selling = Sale(id_transaction, date, quantity, id_product, id_client)
                self.sales_list.append(selling)
                # prev_path = os.path.abspath(os.path.dirname(__file__))  # FOR TESTS
                # transactions_path = os.path.abspath(os.path.dirname(prev_path))  # FOR TESTS
                # classes_path = os.path.abspath(os.path.dirname(transactions_path))  # FOR TESTS
                # products_list_controller = ProductsListController(classes_path + '/storage.txt')  # FOR TESTS
                # product = products_list_controller.get_product_by_id(id_product)  # FOR TESTS
                products_list_controller = ProductsListController()
                product = products_list_controller.get_product_by_id(id_product)
                products_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                              product.price, str(int(product.quantity) - int(quantity)),
                                                              product.volume,
                                                              product.weight)
                return True

    def get_sales_list(self):
        transactions_array = []
        f = open(self.path, 'r')
        for transaction in json.load(f):
            if transaction['is_selling']:
                selling = Sale(transaction['id'],
                               transaction['date'],
                               transaction['quantity'],
                               transaction['id_product'],
                               transaction['id_client'])
                transactions_array.append(selling)
        f.close()
        return transactions_array

    def get_mine_sales_list(self, id_person):
        transactions_array = []
        f = open(self.path, 'r')
        for transaction in json.load(f):
            if transaction['is_selling'] and transaction['id_client'] == id_person:
                selling = Sale(transaction['id'],
                               transaction['date'],
                               transaction['quantity'],
                               transaction['id_product'],
                               transaction['id_client'])
                transactions_array.append(selling)
        f.close()
        return transactions_array

    def get_sale_by_index(self, index):
        if 0 <= index < len(self.sales_list):
            return self.sales_list[index]
        else:
            return None

    def get_mine_sale_by_index(self, index, id_person):
        sales_list = [sale for sale in self.sales_list if sale.id_client == id_person]
        if 0 <= index < len(sales_list):
            return sales_list[index]
        else:
            return None

    def delete_mine_sale_by_index(self, index, id_person):
        sales_list = [sale for sale in self.sales_list if sale.id_client == id_person]
        if 0 <= index < len(sales_list):
            id_transaction = sales_list[index].id_transaction
            if self.is_transaction_ended(id_transaction):
                if bool(random.getrandbits(1)):
                    with open(self.path, 'r') as f:
                        transactions_array = json.load(f)
                        f.close()
                        id_product = ''
                        quantity = ''
                        for transaction in transactions_array:
                            if transaction['id'] == id_transaction:
                                id_product = transaction['id_product']
                                quantity = transaction['quantity']
                                transactions_array.remove(transaction)
                                break
                        j = json.dumps(transactions_array)
                        with open(self.path, 'w') as fw:
                            fw.write(j)
                            fw.close()
                    del sales_list[index]

                    # prev_path = os.path.abspath(os.path.dirname(__file__))  # FOR TESTS
                    # transactions_path = os.path.abspath(os.path.dirname(prev_path))  # FOR TESTS
                    # classes_path = os.path.abspath(os.path.dirname(transactions_path))  # FOR TESTS
                    # products_list_controller = ProductsListController(classes_path + '/storage.txt')  # FOR TESTS
                    # product = products_list_controller.get_product_by_id(id_product)  # FOR TESTS
                    products_list_controller = ProductsListController()
                    product = products_list_controller.get_product_by_id(id_product)
                    products_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                                  product.price, product.quantity + quantity,
                                                                  product.volume,
                                                                  product.weight)
                    return True
                else:
                    return False
            return False
        return False

    def update_sale_by_index(self, index, id_transaction, date, quantity, id_product, id_client, id_person):
        if 0 <= index < len(self.sales_list):
            if self.is_transaction_ended(id_transaction):
                if bool(random.getrandbits(1)):
                    with open(self.path, 'r') as f:
                        transactions_array = json.load(f)
                        f.close()
                        old_quantity = ''
                        for transaction in transactions_array:
                            if transaction['id'] == id_transaction:
                                old_quantity = transaction['quantity']
                                transaction['date'] = date
                                transaction['quantity'] = quantity
                                transaction['id_product'] = id_product
                                transaction['id_client'] = id_client
                                selling = Sale(id_transaction, date, quantity, id_product, id_client)
                                self.sales_list[index] = selling
                                break

                        j = json.dumps(transactions_array)
                        with open(self.path, 'w') as fw:
                            fw.write(j)
                            fw.close()
                    f.close()
                    # prev_path = os.path.abspath(os.path.dirname(__file__))  # FOR TESTS
                    # transactions_path = os.path.abspath(os.path.dirname(prev_path))  # FOR TESTS
                    # classes_path = os.path.abspath(os.path.dirname(transactions_path))  # FOR TESTS
                    # products_list_controller = ProductsListController(classes_path + '/storage.txt')  # FOR TESTS
                    # product = products_list_controller.get_product_by_id(id_product)  # FOR TESTS
                    products_list_controller = ProductsListController()
                    product = products_list_controller.get_product_by_id(id_product)
                    products_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                                  product.price,
                                                                  str(int(product.quantity) +
                                                                      int(old_quantity) - int(quantity)),
                                                                  product.volume, product.weight)
                    return True
                else:
                    return False
            return False
        return False

    def update_mine_sale_by_index(self, index, id_transaction, date, quantity, id_product, id_client, id_person):
        sales_list = [sale for sale in self.sales_list if sale.id_client == id_person]
        if 0 <= index < len(sales_list):
            if self.is_transaction_ended(id_transaction):
                if bool(random.getrandbits(1)):
                    with open(self.path, 'r') as f:
                        transactions_array = json.load(f)
                        f.close()
                        old_quantity = ''
                        for transaction in transactions_array:
                            if transaction['id'] == id_transaction:
                                old_quantity = transaction['quantity']
                                transaction['date'] = date
                                transaction['quantity'] = quantity
                                transaction['id_product'] = id_product
                                transaction['id_client'] = id_client
                                selling = Sale(id_transaction, date, quantity, id_product, id_client)
                                sales_list[index] = selling
                                break

                        j = json.dumps(transactions_array)
                        with open(self.path, 'w') as fw:
                            fw.write(j)
                            fw.close()
                    f.close()

                    # prev_path = os.path.abspath(os.path.dirname(__file__))  # FOR TESTS
                    # transactions_path = os.path.abspath(os.path.dirname(prev_path))  # FOR TESTS
                    # classes_path = os.path.abspath(os.path.dirname(transactions_path))  # FOR TESTS
                    # products_list_controller = ProductsListController(classes_path + '/storage.txt')  # FOR TESTS
                    # product = products_list_controller.get_product_by_id(id_product)  # FOR TESTS
                    products_list_controller = ProductsListController()
                    product = products_list_controller.get_product_by_id(id_product)
                    products_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                                  product.price,
                                                                  str(int(product.quantity) +
                                                                      int(old_quantity) - int(quantity)),
                                                                  product.volume, product.weight)
                    return True
                else:
                    return False
            return False
        return False
