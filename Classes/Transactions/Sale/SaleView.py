from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Transactions.Sale.SaleController import SaleController
from Classes.ProductsList.ProductsListController import ProductsListController
from Classes.Person.CustomersList.CustomersListController import CustomersListController


class SaleView(QWidget):
    def __init__(self, sale, user, index, list_controller, callback, parent=None):
        super(SaleView, self).__init__(parent)
        self.controller = SaleController(sale)
        self.list_controller = list_controller
        self.products_list_controller = ProductsListController()
        self.products_list_controller.get_products_list()
        self.customers_list_controller = CustomersListController()
        self.customers_list_controller.get_customers_list()
        self.sale = sale
        self.index = index
        self.user = user
        self.callback = callback

        is_enabled = user.job == 0

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 300)
        self.setFixedSize(self.size())

        self.create_label("Data", 50, 40)
        day = int(self.controller.get_date()[0] + self.controller.get_date()[1])
        month = int(self.controller.get_date()[3] + self.controller.get_date()[4])
        year = int(self.controller.get_date()[6] + self.controller.get_date()[7] +
                   self.controller.get_date()[8] + self.controller.get_date()[9])
        self.date = self.create_info_label('', False, True, False, QDate(year, month, day))
        self.date.setGeometry(50, 70, 200, 30)

        self.create_label("Quantità", 50, 110)
        self.quantity = self.create_info_label(self.controller.get_quantity(), is_enabled, False, False)
        self.quantity.setGeometry(50, 140, 200, 30)

        self.create_label("Nome Prodotto", 50, 180)
        self.products_list_controller.get_products_list()
        product = self.products_list_controller.get_product_by_id(sale.id_product)
        self.product = self.create_info_label(product.name, False, False, False)
        self.product.setGeometry(50, 210, 200, 30)

        self.create_label("Mail Cliente", 300, 40)
        self.customers_list_controller.get_customers_list()
        print(sale.id_transaction)
        print(sale.id_client)
        customer = self.customers_list_controller.get_customer_by_id(sale.id_client)
        self.customer = self.create_info_label(customer.mail, False, False, False)
        self.customer.setGeometry(300, 70, 200, 30)

        if is_enabled:
            self.update_button = self.create_button('Salva Modifiche')
            self.update_button.clicked.connect(self.update_sale_click)
            self.update_button.setGeometry(340, 155, 120, 35)

            self.delete_button = self.create_button('Cancella Acquisto')
            self.delete_button.clicked.connect(self.delete_sale_click)
            self.delete_button.setGeometry(340, 205, 120, 35)

        self.setWindowTitle('ID Acquisto: ' + self.controller.get_id_transaction())

    def update_sale_click(self):
        self.controller.set_date(self.date.text())
        self.controller.set_quantity(self.quantity.text())

        if self.list_controller.update_mine_sale_by_index(self.index, self.sale.id_transaction, self.date.text(),
                                                          self.quantity.text(), self.sale.id_product, self.sale.id_client,
                                                          self.user.id_person):
            self.callback()
            self.close()
        else:
            message_box = QMessageBox()
            message_box.critical(message_box, 'Errore', "Il prodotto è stato ormai spedito, non può essere annullato",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def delete_sale_click(self):
        message_box = QMessageBox()
        button_reply = message_box.question(message_box, 'Attenzione', "Annullare l'acquisto selezionato?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            if self.list_controller.delete_mine_sale_by_index(self.index, self.user.id_person):
                self.callback()
                self.close()
            else:
                message_box.critical(message_box, 'Errore',
                                     "Il prodotto è stato ormai spedito, non può essere annullato",
                                     QMessageBox.Ok, QMessageBox.Ok)

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 150, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

    def create_info_label(self, text, is_enabled, is_date, is_password, date=QDate(2000, 1, 1)):
        if is_date:
            info_label = QDateEdit(self)
            info_label.setDate(date)
            info_label.setDisplayFormat("dd/MM/yyyy")
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            return info_label
        else:
            info_label = QLineEdit(self)
            info_label.setText(text)
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            if is_password:
                info_label.setEchoMode(QLineEdit.Password)
            return info_label

    def create_button(self, text):
        button = QPushButton(self)
        font_button = QFont("Helvetica", 12, QFont.Bold)
        button.setFont(font_button)
        button.setText(text)
        button.setStyleSheet(self.stylesheet)
        return button
