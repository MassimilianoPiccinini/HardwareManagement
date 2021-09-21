from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from datetime import datetime

from Classes.ProductsList.ProductsListController import ProductsListController
from Classes.Person.CustomersList.CustomersListController import CustomersListController


class AddSaleView(QWidget):
    def __init__(self, controller, user, callback):
        super(AddSaleView, self).__init__()
        self.controller = controller
        self.callback = callback
        self.products_list_controller = ProductsListController()
        self.customers_list_controller = CustomersListController()
        self.user = user

        is_enabled = user.job == 0

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 300)
        self.setFixedSize(self.size())

        self.create_label("Quantità", 50, 40)
        self.quantity = self.create_info_label(is_enabled, 1, False)
        self.quantity.setGeometry(50, 70, 200, 30)
        self.quantity.textChanged.connect(self.on_change_text)

        self.create_label("Prodotto", 50, 110)
        self.product = self.create_info_label(is_enabled, 2, False)
        self.product.setGeometry(50, 140, 200, 30)
        self.product.currentIndexChanged.connect(self.on_change_text)

        self.create_label("Prezzo", 300, 40)
        self.price = QLabel(self)
        font = QFont("Helvetica", 12, QFont.Bold)
        self.price.setFont(font)
        self.price.setText('€ 0')
        self.price.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px; background-color: white')
        self.price.setGeometry(300, 70, 200, 30)

        self.create_button = self.create_button('Completa Acquisto')
        self.create_button.clicked.connect(self.add_sale_click)
        self.create_button.setGeometry(340, 205, 120, 35)

        self.setWindowTitle("Nuovo Acquisto")

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
                    info_label.addItem(str(product.id_product) + ' - ' + str(product.name))
            else:
                for customer in self.customers_list_controller.get_customers_list():
                    info_label.addItem(str(customer.id_person) + ' - ' + str(customer.name))
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

    def add_sale_click(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        quantity = self.quantity.text()
        product = self.product.currentText()
        product = product.split()
        id_product = product[0]
        id_customer = self.user.id_person

        my_product = self.products_list_controller.get_product_by_id(id_product)

        if date == "" or quantity == "" or id_product == "" or id_customer == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif int(quantity) <= 0:
            QMessageBox.critical(self, 'Errore', 'La quantità deve essere maggiore di zero (> 0)',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif int(quantity) > int(my_product.quantity):
            QMessageBox.critical(self, 'Errore', 'Le quantità richieste non sono al momento disponibili',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif self.user.payment_method == 0 and (self.user.credit_card_number == "" or self.user.valid_through == ""
                                                or self.user.ccv == ""):
            QMessageBox.critical(self, 'Errore', 'Il metodo di pagamento predefinito (carta di credito) non è stato '
                                                 'impostato',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif self.user.payment_method == 1 and (self.user.iban == ""):
            QMessageBox.critical(self, 'Errore', 'Il metodo di pagamento predefinito (conto corrente) non è stato '
                                             'impostato',
                             QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.create_sale(date, quantity, id_product, id_customer)
            self.callback()
            self.close()

    def on_change_text(self):
        quantity = 0
        if self.quantity.text() != "":
            quantity = int(self.quantity.text())
        product = self.product.currentText()  # self.product.selectedItems()[0].text()
        product = product.split()
        id_product = product[0]
        my_product = self.products_list_controller.get_product_by_id(id_product)

        self.price.setText('€ ' + str(int(quantity) * int(my_product.price)))