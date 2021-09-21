from unittest import TestCase

from Classes.Transactions.Sale.Sale import Sale
from Classes.Transactions.SalesList.SalesListController import SalesListController

import os


class TestSalesListController(TestCase):
    # TODO: delete real sale
    def test_create_sale(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        transactions_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SalesListController(transactions_path + '/transactions.txt')
        # TODO: change 10 to 1001 if we want the test fails
        success = controller.create_sale("11/07/2021", "10", "HB653JKD", "2c61a923")
        self.assertTrue(success)

    def test_get_sale_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        transactions_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SalesListController(transactions_path + '/transactions.txt')
        sale = controller.get_sale_by_index(0)
        my_sale = Sale("9031146", "13/07/2021", "10", "HB653JKD", "XJ410K73J532")
        self.assertEqual(sale.date, my_sale.date)
        self.assertEqual(sale.quantity, my_sale.quantity)

    def test_update_mine_sale_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        transactions_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SalesListController(transactions_path + '/transactions.txt')
        success = controller.update_mine_sale_by_index(0, "9031146", "13/07/2021", "20", "HB653JKD", "XJ410K73J532",
                                                       "2c61a923")
        if success:
            self.assertTrue(success)
        else:
            print('La vendita non può essere modificata perchè il prodotto è stato già spedito')
            self.fail()

    def test_delete_mine_sale_by_index(self):
        prev_path = os.path.abspath(os.path.dirname(__file__))
        transactions_path = os.path.abspath(os.path.dirname(prev_path))
        controller = SalesListController(transactions_path + '/transactions.txt')
        controller.delete_mine_sale_by_index(9, "2c61a923")
