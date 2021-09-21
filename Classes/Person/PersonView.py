from Classes.Person.PersonController import PersonController
from Classes.PeopleList.PeopleListController import PeopleListController
from Classes.Person.Customer.CustomerController import CustomerController
from Classes.Person.CustomersList.CustomersListController import CustomersListController
from Classes.Person.Employee.EmployeeController import EmployeeController
from Classes.Person.EmployeesList.EmployeesListController import EmployeesListController

from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PersonView(QWidget):

    def __init__(self, user, parent=None):
        super(PersonView, self).__init__(parent)

        self.user = user

        self.controller = PersonController(user)
        self.people_list_controller = PeopleListController()
        self.people_list_controller.get_people_list()
        self.customer_controller = CustomerController(user)
        self.customers_list_controller = CustomersListController()
        self.customers_list_controller.get_customers_list()
        self.employee_controller = EmployeeController(user)
        self.employees_list_controller = EmployeesListController()
        self.employees_list_controller.get_employees_list()

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 550)
        self.setFixedSize(self.size())

        self.create_label("Nome", 50, 50)
        self.name = self.create_info_label(self.controller.get_name(), 1, False)
        self.name.setGeometry(50, 80, 200, 30)

        self.create_label("Cognome", 50, 120)
        self.surname = self.create_info_label(self.controller.get_surname(), 1, False)
        self.surname.setGeometry(50, 150, 200, 30)

        self.create_label("Email", 50, 190)
        self.email = self.create_info_label(self.controller.get_mail(), 1, False)
        self.email.setGeometry(50, 220, 200, 30)

        self.create_label("Password", 50, 260)
        self.password = self.create_info_label(self.controller.get_password(), 1, True)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(50, 290, 200, 30)

        self.create_label("Data di Nascita", 50, 330)
        day = int(self.controller.get_date_of_birth()[0] + self.controller.get_date_of_birth()[1])
        month = int(self.controller.get_date_of_birth()[3] + self.controller.get_date_of_birth()[4])
        year = int(self.controller.get_date_of_birth()[6] + self.controller.get_date_of_birth()[7] +
                   self.controller.get_date_of_birth()[8] + self.controller.get_date_of_birth()[9])
        self.date_of_birth = self.create_info_label('', 0, False, QDate(year, month, day))
        self.date_of_birth.setGeometry(50, 360, 200, 30)

        self.create_label("Luogo di Nascita", 50, 400)
        self.place_of_birth = self.create_info_label(self.controller.get_place_of_birth(), 1, False)
        self.place_of_birth.setGeometry(50, 430, 200, 30)

        self.create_label("Numero di Telefono", 50, 470)
        self.phone_number = self.create_info_label(self.controller.get_phone_number(), 1, False)
        self.phone_number.setGeometry(50, 500, 200, 30)

        self.create_label("Indirizzo", 300, 50)
        self.address = self.create_info_label(self.controller.get_address(), 1, False)
        self.address.setGeometry(300, 80, 200, 30)

        if self.user.job == 0:
            self.create_label("Metodo di Pagamento predefinito", 300, 120)
            self.payment_method = self.create_info_label(self.customer_controller.get_payment_method(), 2, False)
            self.payment_method.setGeometry(300, 150, 200, 30)

            self.create_label("Numero Carta di Credito", 300, 190)
            self.credit_card_number = self.create_info_label(self.customer_controller.get_credit_card_number(), 1, False)
            self.credit_card_number.setGeometry(300, 220, 200, 30)

            self.create_label("Valida fino a", 300, 260)
            self.valid_through = self.create_info_label(self.customer_controller.get_valid_through(), 1, False)
            self.valid_through.setGeometry(300, 290, 200, 30)

            self.create_label("CCV", 300, 330)
            self.ccv = self.create_info_label(self.customer_controller.get_ccv(), 1, False)
            self.ccv.setGeometry(300, 360, 200, 30)

            self.create_label("IBAN", 300, 400)
            self.iban = self.create_info_label(self.customer_controller.get_iban(), 1, False)
            self.iban.setGeometry(300, 430, 200, 30)

        self.button_save = QPushButton(self)
        font_button = QFont("Helvetica", 12, QFont.Bold)
        self.button_save.setFont(font_button)
        self.button_save.setText("Salva")
        self.button_save.setStyleSheet(self.stylesheet)
        self.button_save.clicked.connect(self.go_save)
        self.button_save.setGeometry(340, 495, 120, 35)

        self.setWindowTitle("Registrazione")

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 200, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

        # def get_form_entry(self, index, label):
        #    self.v_layout.addWidget(QLabel(label))
        #    current_text_edit = QLineEdit(self)
        #    self.v_layout.addWidget(current_text_edit)
        #    self.info[index] = current_text_edit

    def create_info_label(self, text, data_type, is_password, date=QDate(2000, 1, 1)):
        if data_type == 0:
            info_label = QDateEdit(self)
            info_label.setDate(date)
            info_label.setDisplayFormat("dd/MM/yyyy")
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            return info_label
        elif data_type == 1:
            info_label = QLineEdit(self)
            info_label.setText(str(text))
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            if is_password:
                info_label.setEchoMode(QLineEdit.Password)
            return info_label
        else:
            info_label = QComboBox(self)
            info_label.addItem("Carta di Credito")
            info_label.addItem("Contro Corrente")
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; bsale-radius: 8px;')
            return info_label

    def go_save(self):
        if self.name.text() == '' or self.surname.text() == '' or self.surname.text() == '' or self.surname.text() == '' or self.surname.text() == '' or self.surname.text() == '' or self.surname.text() == '' or self.surname.text() == '':
            message_box = QMessageBox()
            message_box.critical(message_box, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.set_name(self.name.text())
            self.controller.set_surname(self.surname.text())
            self.controller.set_mail(self.email.text())
            self.controller.set_password(self.password.text())
            self.controller.set_date_of_birth(self.date_of_birth.text())
            self.controller.set_place_of_birth(self.place_of_birth.text())
            self.controller.set_phone_number(self.phone_number.text())
            self.controller.set_address(self.address.text())
            if self.user.job == 0:
                is_credit_card = self.payment_method.currentText() == "Carta di Credito" # .selectedItems()[0].text() == "Carta di Credito"
                self.customer_controller.set_payment_method(0 if is_credit_card else 1)
                self.customer_controller.set_credit_card_number(self.credit_card_number.text())
                self.customer_controller.set_valid_through(self.valid_through.text())
                self.customer_controller.set_ccv(self.ccv.text())
                self.customer_controller.set_iban(self.iban.text())
                self.customers_list_controller.update_customer_by_id(self.controller.get_id(), self.name.text(),
                                                                     self.surname.text(), self.email.text(),
                                                                     self.password.text(), self.date_of_birth.text(),
                                                                     self.place_of_birth.text(),
                                                                     self.phone_number.text(), self.address.text(), 2,
                                                                     0 if is_credit_card else 1,
                                                                     self.credit_card_number.text(), 0,
                                                                     self.valid_through.text(), self.ccv.text(),
                                                                     self.iban.text())
                self.close()
            else:
                self.people_list_controller.update_person_by_id(self.controller.get_id(), self.name.text(),
                                                                self.surname.text(), self.email.text(),
                                                                self.password.text(), self.date_of_birth.text(),
                                                                self.place_of_birth.text(), self.phone_number.text(),
                                                                self.address.text(), 2)
                self.close()



