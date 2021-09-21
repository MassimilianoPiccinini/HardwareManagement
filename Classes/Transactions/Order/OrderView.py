from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Transactions.Order.OrderController import OrderController
from Classes.ProductsList.ProductsListController import ProductsListController
from Classes.SuppliersList.SuppliersListController import SuppliersListController
from Classes.Transactions.OrdersList.OrdersListController import OrdersListController


class OrderView(QWidget):
    def __init__(self, order, user, index, list_controller, callback, parent=None):
        super(OrderView, self).__init__(parent)
        self.controller = OrderController(order)
        self.list_controller = list_controller
        self.products_list_controller = ProductsListController()
        self.products_list_controller.get_products_list()
        self.suppliers_list_controller = SuppliersListController()
        self.suppliers_list_controller.get_suppliers_list()
        self.order = order
        self.index = index
        self.callback = callback

        is_enabled = user.job == 2

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
        product = self.products_list_controller.get_product_by_id(order.id_product)
        self.product = self.create_info_label(product.name, False, False, False)
        self.product.setGeometry(50, 210, 200, 30)

        self.create_label("Nome Fornitore", 300, 40)
        self.suppliers_list_controller.get_suppliers_list()
        supplier = self.suppliers_list_controller.get_supplier_by_id(order.id_supplier)
        self.supplier = self.create_info_label(supplier.name, False, False, False)
        self.supplier.setGeometry(300, 70, 200, 30)

        if is_enabled:
            self.update_button = self.create_button('Salva Modifiche')
            self.update_button.clicked.connect(self.update_order_click)
            self.update_button.setGeometry(340, 155, 120, 35)

            self.delete_button = self.create_button('Cancella Ordine')
            self.delete_button.clicked.connect(self.delete_order_click)
            self.delete_button.setGeometry(340, 205, 120, 35)

        self.setWindowTitle('ID Ordine: ' + self.controller.get_id_transaction())

    def update_order_click(self):
        self.controller.set_date(self.date.text())
        self.controller.set_quantity(self.quantity.text())

        if self.list_controller.update_order_by_index(self.index, self.order.id_transaction, self.date.text(),
                                                      self.quantity.text(), self.order.id_product,
                                                      self.order.id_supplier):
            self.callback()
            self.close()
        else:
            message_box = QMessageBox()
            message_box.critical(message_box, 'Errore', "L'ordine è stato ormai spedito, non può essere annullato",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def delete_order_click(self):
        message_box = QMessageBox()
        button_reply = message_box.question(message_box, 'Attenzione', "Annullare l'ordine selezionato?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            if self.list_controller.delete_order_by_index(self.index):
                self.callback()
                self.close()
            else:
                message_box.critical(message_box, 'Errore', "L'ordine è stato ormai spedito, non può essere annullato",
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
