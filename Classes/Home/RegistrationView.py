from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from Classes.Home import LoginView
from Classes.Person.CustomersList.CustomersListController import CustomersListController
import json


class RegistrationView(QWidget):
    def __init__(self):
        super(RegistrationView, self).__init__()
        # self.login_view = LoginView()
        self.controller = self.controller = CustomersListController()
        # self.callback = callback
        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 550)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni del nuovo dipendente.

        self.create_label("Nome", 50, 50)
        self.name = QLineEdit(self)
        self.name.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.name.setGeometry(50, 80, 200, 30)

        self.create_label("Cognome", 50, 120)
        self.surname = QLineEdit(self)
        self.surname.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.surname.setGeometry(50, 150, 200, 30)

        self.create_label("Email", 50, 190)
        self.email = QLineEdit(self)
        self.email.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.email.setGeometry(50, 220, 200, 30)

        self.create_label("Password", 50, 260)
        self.password = QLineEdit(self)
        self.password.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(50, 290, 200, 30)

        self.create_label("Data di Nascita", 50, 330)
        self.birth_date = QDateEdit(self)
        self.birth_date.setDisplayFormat("dd/MM/yyyy")
        self.birth_date.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.birth_date.setGeometry(50, 360, 200, 30)

        self.create_label("Luogo di Nascita", 50, 400)
        self.birth_place = QLineEdit(self)
        self.birth_place.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.birth_place.setGeometry(50, 430, 200, 30)

        self.create_label("Numero di Telefono", 300, 50)
        self.phone_number = QLineEdit(self)
        self.phone_number.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.phone_number.setGeometry(300, 80, 200, 30)

        self.create_label("Indirizzo", 300, 120)
        self.address = QLineEdit(self)
        self.address.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.address.setGeometry(300, 150, 200, 30)

        self.button_login = QPushButton(self)
        font_button = QFont("Helvetica", 12, QFont.Bold)
        self.button_login.setFont(font_button)
        self.button_login.setText("Registrami")
        self.button_login.setStyleSheet(self.stylesheet)
        self.button_login.clicked.connect(self.sign_up)
        self.button_login.setGeometry(340, 365, 120, 35)

        self.button_login = QPushButton(self)
        self.button_login.setFont(font_button)
        self.button_login.setText("Home")
        self.button_login.setStyleSheet(self.stylesheet)
        self.button_login.clicked.connect(self.go_login_view)
        self.button_login.setGeometry(340, 425, 120, 35)

        self.setWindowTitle("Registrazione")

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 150, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

    # def get_form_entry(self, index, label):
    #    self.v_layout.addWidget(QLabel(label))
    #    current_text_edit = QLineEdit(self)
    #    self.v_layout.addWidget(current_text_edit)
    #    self.info[index] = current_text_edit

    def go_login_view(self):
        # print(self.login_view)
        self.login_view = LoginView.LoginView()
        self.login_view.show()
        self.close()

    def sign_up(self):

        name = self.name.text().strip()
        surname = self.surname.text().strip()
        email = self.email.text().strip().lower()
        password = self.password.text().strip()
        birth_date = self.birth_date.text().strip()
        birth_place = self.birth_place.text().strip()
        phone_number = self.phone_number.text().strip()
        address = self.address.text().strip()
        if name != '' and surname != '' and email != '' and password != '' and birth_place != '' and birth_place != ''\
                and phone_number != '' and address != '':
            if self.controller.create_customer(name, surname, email, password, birth_date, birth_place, phone_number,
                                               address, 0, '', '', 0, '', '', ''):
                self.hide()
                self.go_login_view()
                self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)