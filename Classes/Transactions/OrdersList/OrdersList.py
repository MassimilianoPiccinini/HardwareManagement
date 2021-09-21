import json
import uuid
import random

from Classes.Transactions.Order.Order import Order
from Classes.ProductsList.ProductsListController import ProductsListController


def generate_id():
    uid = uuid.uuid4()
    return uid.hex[0:8]


def is_transaction_ended(self, id_transaction):
    with open("Classes/Transactions/transactions.txt", 'r') as f:
        for transaction in json.load(f):
            if transaction['id'] == id_transaction:
                return True
        f.close()
        return False


class OrdersList:

    def __init__(self):
        super(OrdersList, self).__init__()
        self.orders_list = self.get_orders_list()

    def create_order(self, date, quantity, id_product, id_supplier):
        with open("Classes/Transactions/transactions.txt", 'r') as fr:
            transactions_array = json.load(fr)
            fr.close()
            id_transaction = generate_id()
            new_user = {
                'id': id_transaction,
                'date': date,
                'quantity': quantity,
                'id_product': id_product,
                'id_supplier': id_supplier,
                'is_selling': False
            }
            transactions_array.append(new_user)

            j = json.dumps(transactions_array)
            with open("Classes/Transactions/transactions.txt", 'w') as fw:
                fw.write(j)
                fw.close()
                order = Order(id_transaction, date, quantity, id_product, id_supplier)
                self.orders_list.append(order)
                product_list_controller = ProductsListController()
                product = product_list_controller.get_product_by_id(id_product)
                product_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                             product.price, str(int(product.quantity) + int(quantity)),
                                                             product.volume, product.weight)
                return True

    def get_orders_list(self):
        transactions_array = []
        with open("Classes/Transactions/transactions.txt", 'r') as f:
            for transaction in json.load(f):
                if not transaction['is_selling']:
                    order = Order(transaction['id'],
                                  transaction['date'],
                                  transaction['quantity'],
                                  transaction['id_product'],
                                  transaction['id_supplier'])
                    transactions_array.append(order)
        return transactions_array

    def get_order_by_index(self, index):
        if 0 <= index < len(self.orders_list):
            return self.orders_list[index]
        else:
            return None

    def delete_order_by_index(self, index):
        if 0 <= index < len(self.orders_list):
            id_transaction = self.orders_list[index].id_transaction
            if is_transaction_ended(self, id_transaction):
                if bool(random.getrandbits(1)):
                    with open("Classes/Transactions/transactions.txt", 'r') as f:
                        transactions_array = json.load(f)
                        id_product = ''
                        quantity = ''
                        for transaction in transactions_array:
                            if transaction['id'] == id_transaction:
                                id_product = transaction['id_product']
                                quantity = transaction['quantity']
                                transactions_array.remove(transaction)
                                break
                        j = json.dumps(transactions_array)
                        with open("Classes/Transactions/transactions.txt", 'w') as fw:
                            fw.write(j)
                            fw.close()
                    del self.orders_list[index]
                    product_list_controller = ProductsListController()
                    product = product_list_controller.get_product_by_id(id_product)
                    product_list_controller.update_product_by_id(id_product, product.name,
                                                                 product.description, product.price,
                                                                 str(int(product.quantity) - int(quantity)),
                                                                 product.volume, product.weight)
                    return True
                else:
                    return False
            return False
        return False

    def update_order_by_index(self, index, id_transaction, date, quantity, id_product, id_supplier):
        if 0 <= index < len(self.orders_list):
            if is_transaction_ended(self, id_transaction):
                if bool(random.getrandbits(1)):
                    with open("Classes/Transactions/transactions.txt", 'r') as f:
                        transactions_array = json.load(f)
                        old_quantity = ''
                        for transaction in transactions_array:
                            if transaction['id'] == id_transaction:
                                old_quantity = transaction['quantity']
                                transaction['date'] = date
                                transaction['quantity'] = quantity
                                transaction['id_product'] = id_product
                                transaction['id_supplier'] = id_supplier
                                order = Order(id_transaction, date, quantity, id_product, id_supplier)
                                transactions_array[index] = {
                                    'id': id_transaction,
                                    'date': date,
                                    'quantity': quantity,
                                    'id_product': id_product,
                                    'id_supplier': id_supplier,
                                    'is_selling': False
                                }
                                self.orders_list[index] = order
                                break

                        j = json.dumps(transactions_array)
                        with open("Classes/Transactions/transactions.txt", 'w') as fw:
                            fw.write(j)
                            fw.close()
                    f.close()
                    products_list_controller = ProductsListController()
                    product = products_list_controller.get_product_by_id(id_product)
                    products_list_controller.update_product_by_id(id_product, product.name, product.description,
                                                                  product.price,
                                                                  str(int(product.quantity) - int(old_quantity) +
                                                                      int(quantity)),
                                                                  product.volume, product.weight)
                    return True
                else:
                    return False
            return False
        return False
