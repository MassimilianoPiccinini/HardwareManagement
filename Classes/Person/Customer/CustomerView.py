from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Person.Customer.CustomerController import CustomerController


class CustomerView(QWidget):
    def __init__(self, customer, user, index, list_controller, parent=None):
        super(CustomerView, self).__init__(parent)
        self.controller = CustomerController(customer)
        self.list_controller = list_controller
        self.customer = customer
        self.index = index

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 550)
        self.setFixedSize(self.size())

        self.create_label("Nome", 50, 40)
        self.name = self.create_info_label(self.controller.get_name(), False, False, False)
        self.name.setGeometry(50, 70, 200, 30)

        self.create_label("Cognome", 50, 110)
        self.surname = self.create_info_label(self.controller.get_surname(), False, False, False)
        self.surname.setGeometry(50, 140, 200, 30)

        self.create_label("email", 50, 180)
        self.email = self.create_info_label(self.controller.get_mail(), False, False, False)
        self.email.setGeometry(50, 210, 200, 30)

        self.create_label("Data di Nascita", 50, 250)
        day = int(self.controller.get_date_of_birth()[0] + self.controller.get_date_of_birth()[1])
        month = int(self.controller.get_date_of_birth()[3] + self.controller.get_date_of_birth()[4])
        year = int(self.controller.get_date_of_birth()[6] + self.controller.get_date_of_birth()[7] +
                   self.controller.get_date_of_birth()[8] + self.controller.get_date_of_birth()[9])
        self.date_of_birth = self.create_info_label('', False, True, False, QDate(year, month, day))
        self.date_of_birth.setGeometry(50, 280, 200, 30)

        self.create_label("Luogo di Nascita", 50, 320)
        self.place_of_birth = self.create_info_label(self.controller.get_place_of_birth(), False, False, False)
        self.place_of_birth.setGeometry(50, 350, 200, 30)

        self.create_label("Numero di Telefono", 50, 390)
        self.phone_number = self.create_info_label(self.controller.get_phone_number(), False, False, False)
        self.phone_number.setGeometry(50, 420, 200, 30)

        self.create_label("Indirizzo", 300, 40)
        self.address = self.create_info_label(self.controller.get_address(), False, False, False)
        self.address.setGeometry(300, 70, 200, 30)

        self.create_label('Ha un Metodo di Pagamento', 300, 110)
        has_payment_method = self.controller.get_iban() != '' or self.controller.get_credit_card_number() != ''
        has_payment_method_str = ''
        if has_payment_method:
            has_payment_method_str = 'Si'
        else:
            has_payment_method_str = 'No'
        self.has_payment_method = self.create_info_label(has_payment_method_str, False, False, False)
        self.has_payment_method.setGeometry(300, 140, 200, 30)

        self.setWindowTitle(self.controller.get_name() + ' ' + self.controller.get_surname())

    def update_customer_click(self):
        self.controller.set_name(self.name.text())
        self.controller.set_surname(self.surname.text())
        self.controller.set_mail(self.email.text())
        self.controller.set_date_of_birth(self.date_of_birth.text())
        self.controller.set_place_of_birth(self.place_of_birth.text())
        self.controller.set_phone_number(self.phone_number.text())
        self.controller.set_address(self.address.text())

        self.list_controller.update_customer_by_index(self.index, self.customer.id_person, self.name.text(),
                                                      self.surname.text(), self.email.text(),
                                                      self.customer.password, self.date_of_birth.text(),
                                                      self.place_of_birth.text(), self.phone_number.text(),
                                                      self.address.text(), 0, self.customer.payment_method,
                                                      self.customer.credit_card_number, self.customer.permissions,
                                                      self.customer.valid_through, self.customer.ccv,
                                                      self.customer.iban)
        self.close()

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 180, 30)
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
