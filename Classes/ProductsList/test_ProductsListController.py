from unittest import TestCase

from Classes.Product.Product import Product
from Classes.ProductsList.ProductsListController import ProductsListController

import os


# TODO: in order to execute tests, we must change the path directory manually, because the test path is different from
# TODO: the file path that is called. So the changes must be done both in controller and in model, uncommenting rows
# TODO: with the comment : FOR TESTS

class TestProductsListController(TestCase):
    def test_get_product_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        self.controller = ProductsListController(classes_path + '/storage.txt')
        self.product = Product('HB653JKD', 'Vite', 'Vite molto bella', '30', '359', '0.5', '3')
        self.my_product = self.controller.get_product_by_index(0)
        self.assertEqual(self.product.id_product, self.my_product.id_product)
        self.assertEqual(self.product.name, self.my_product.name)
        self.assertEqual(self.product.description, self.my_product.description)
        self.assertEqual(self.product.price, self.my_product.price)
        self.assertEqual(self.product.weight, self.my_product.weight)
        self.assertEqual(self.product.volume, self.my_product.volume)

    def test_get_product_by_id(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        self.controller = ProductsListController(classes_path + '/storage.txt')
        self.product = Product('HB653JKD', 'Vite', 'Vite molto bella', '30', '359', '0.5', '3')
        self.my_product = self.controller.get_product_by_id('HB653JKD')
        self.assertEqual(self.product.id_product, self.my_product.id_product)
        self.assertEqual(self.product.name, self.my_product.name)
        self.assertEqual(self.product.description, self.my_product.description)
        self.assertEqual(self.product.price, self.my_product.price)
        self.assertEqual(self.product.weight, self.my_product.weight)
        self.assertEqual(self.product.volume, self.my_product.volume)

    def test_update_product_by_id(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        self.controller = ProductsListController(classes_path + '/storage.txt')
        self.product = Product('HB653JKD', 'Vite', 'Vite molto bella', '30', '359', '0.5', '3')
        self.assertTrue(self.controller.update_product_by_id('HB653JKD', 'Vite', 'Vite molto bella', '30', '1000',
                                                             '0.5', '3'))

    def test_search_by_name(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        classes_path = os.path.abspath(os.path.dirname(prev_path))
        self.controller = ProductsListController(classes_path + '/storage.txt')
        self.product = Product('HB653JKD', 'Vite', 'Vite molto bella', '30', '1000', '0.5', '3')
        self.my_product = self.controller.search_by_name("vit")[0]
        self.assertEqual(self.product.id_product, self.my_product.id_product)
        self.assertEqual(self.product.name, self.my_product.name)
        self.assertEqual(self.product.description, self.my_product.description)
        self.assertEqual(self.product.price, self.my_product.price)
        self.assertEqual(self.product.weight, self.my_product.weight)
        self.assertEqual(self.product.volume, self.my_product.volume)
