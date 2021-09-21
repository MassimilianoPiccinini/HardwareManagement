from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Product.ProductController import ProductController
from Classes.ProductsList.ProductsListController import ProductsListController


class ProductView(QWidget):
    def __init__(self, product, user, index, list_controller, parent=None):
        super(ProductView, self).__init__(parent)
        self.controller = ProductController(product)
        self.list_controller = list_controller
        self.product = product
        self.index = index

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 300)
        self.setFixedSize(self.size())

        self.create_label("Nome", 50, 40)
        self.name = self.create_info_label(self.controller.get_name(), False, False, False)
        self.name.setGeometry(50, 70, 200, 30)

        self.create_label("Descrizione", 50, 110)
        self.description = self.create_info_plain_label(self.controller.get_description(), False)
        self.description.setGeometry(50, 140, 200, 70)

        self.create_label("Prezzo in €", 50, 220)
        self.price = self.create_info_label(self.controller.get_price(), False, False, False)
        self.price.setGeometry(50, 250, 200, 30)

        self.create_label("Quantità Disponibile", 300, 40)
        self.quantity = self.create_info_label(self.controller.get_quantity(), False, False, False)
        self.quantity.setGeometry(300, 70, 200, 30)

        self.create_label("Volume", 300, 110)
        self.volume = self.create_info_label(self.controller.get_volume(), False, False, False)
        self.volume.setGeometry(300, 140, 200, 30)

        self.create_label("Peso", 300, 180)
        self.weight = self.create_info_label(self.controller.get_weight(), False, False, False)
        self.weight.setGeometry(300, 210, 200, 30)

        self.setWindowTitle(self.controller.get_name())

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 150, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

    def create_info_plain_label(self, text, is_enabled):
        info_label = QPlainTextEdit(self)
        info_label.setPlainText(text)
        info_label.setEnabled(is_enabled)
        font = QFont("Helvetica", 12, QFont.Bold)
        info_label.setFont(font)
        info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px; background-color: white')
        return info_label

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
