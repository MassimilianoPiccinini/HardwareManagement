from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from datetime import datetime

from Classes.Transactions.Order import OrderController
from Classes.ProductsList.ProductsListController import ProductsListController
from Classes.SuppliersList.SuppliersListController import SuppliersListController


class AddOrderView(QWidget):
    def __init__(self, controller, user, callback):
        super(AddOrderView, self).__init__()
        self.controller = controller
        self.callback = callback
        self.products_list_controller = ProductsListController()
        self.suppliers_list_controller = SuppliersListController()
        is_enabled = user.job == 2

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 300)
        self.setFixedSize(self.size())

        self.create_label("Quantità", 50, 40)
        self.quantity = self.create_info_label(is_enabled, 1, False)
        self.quantity.setGeometry(50, 70, 200, 30)

        self.create_label("Prodotto", 50, 110)
        self.product = self.create_info_label(is_enabled, 2, False)
        self.product.setGeometry(50, 140, 200, 30)

        self.create_label("Fornitore", 300, 40)
        self.supplier = self.create_info_label(is_enabled, 2, True, False)
        self.supplier.setGeometry(300, 70, 200, 30)

        self.create_button = self.create_button('Completa Ordine')
        self.create_button.clicked.connect(self.add_order_click)
        self.create_button.setGeometry(340, 205, 120, 35)

        self.setWindowTitle("Nuovo Ordine")

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 150, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

    def create_info_label(self, is_enabled, data_type, is_password, is_product=True):
        if data_type == 0:
            info_label = QDateEdit(self)
            info_label.setDisplayFormat("dd/MM/yyyy")
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            return info_label
        elif data_type == 1:
            info_label = QLineEdit(self)
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            if is_password:
                info_label.setEchoMode(QLineEdit.Password)
            return info_label
        else:
            info_label = QComboBox(self)
            if is_product:
                for product in self.products_list_controller.get_products_list():
                    info_label.addItem(str(str(product.id_product) + ' - ' + str(product.name)))
            else:
                for supplier in self.suppliers_list_controller.get_suppliers_list():
                    info_label.addItem(str(str(supplier.id_supplier) + ' - ' + str(supplier.name)))
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            return info_label

    def create_button(self, text):
        button = QPushButton(self)
        font_button = QFont("Helvetica", 12, QFont.Bold)
        button.setFont(font_button)
        button.setText(text)
        button.setStyleSheet(self.stylesheet)
        return button

    def add_order_click(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        quantity = self.quantity.text()
        if quantity.isnumeric():
            # product = self.product.selectedItems()[0].text()
            product = self.product.currentText()
            product = product.split()
            id_product = product[0]
            # supplier = self.supplier.selectedItems()[0].text()
            supplier = self.supplier.currentText()
            supplier = supplier.split()
            id_supplier = supplier[0]
            if date == "" or quantity == "" or id_product == "" or id_supplier == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controller.create_order(date, quantity, id_product, id_supplier)
                self.callback()
                self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Inserisci una quantità valida',
                                 QMessageBox.Ok, QMessageBox.Ok)
