from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Classes.Home import HomeView
from Classes.Person.Customer.Customer import Customer
from Classes.Person.CustomersList.CustomersListController import CustomersListController
import json

from Classes.Home.RegistrationView import RegistrationView
from Classes.Person.Employee.Employee import Employee
from Classes.Person.Person import Person


class LoginView(QWidget):
    def __init__(self):
        super(LoginView, self).__init__()

        self.controller = self.controller = CustomersListController()
        # self.callback = callback
        self.info = {}
        # self.stylesheet = """QPushButton{}"""
        self.resize(250, 400)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        image_path = "Images/FerramentaBertiLogo.jpg"
        image = QImage(image_path)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True)
        self.label.setStyleSheet('border-radius: 10px;')
        self.label.setGeometry(75, 10, 100, 100)

        # Inserimento e impostazioni grafiche dell'etichetta 'Username', dell'icona per l'username
        # e della casella di testo per inserire l'username.
        self.username = QLineEdit(self)  # usare questa label.text() per prendere i dati nella tabella
        self.username.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.username.setPlaceholderText("username")
        self.username.setGeometry(25, 120, 200, 40)

        # Inserimento e impostazioni grafiche dell'etichetta 'Password', dell'icona della password
        # e della casella di testo per inserire la password.
        self.password = QLineEdit(self)  # usare questa label.text() per prendere i dati nella tabella
        self.password.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("password")
        self.password.setGeometry(25, 170, 200, 40)
        # self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # btn_ok = QPushButton("OK")
        # btn_ok.clicked.connect(self.login)
        # self.v_layout.addWidget(btn_ok)
        self.button_login = QPushButton(self)
        font_button = QFont('Helvetica', 15, QFont.Bold)
        self.button_login.setFont(font_button)
        self.button_login.setText("Log In")
        self.button_login.setStyleSheet('border-radius: 15px;background-color: #228B22;color: white;')
        self.button_login.clicked.connect(self.login)
        self.button_login.setGeometry(65, 250, 120, 35)

        # btn_Registrati = QPushButton("Registrati")
        # btn_Registrati.clicked.connect(self.go_registration_view)
        # self.v_layout.addWidget(btn_Registrati)
        self.button_signup = QPushButton(self)
        self.button_signup.setFont(font_button)
        self.button_signup.setText("Registrati")
        self.button_signup.setStyleSheet('border-radius: 15px;background-color: #228B22;color: white;')
        self.button_signup.clicked.connect(self.go_registration_view)
        self.button_signup.setGeometry(65, 300, 120, 35)

        # self.setLayout(self.v_layout)
        self.setWindowTitle("Log In")

    def get_form_entry(self, index, label):
        self.v_layout.addWidget(QLabel(label))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[index] = current_text_edit

    def go_registration_view(self):

        self.hide()
        self.registration_view = RegistrationView()
        self.registration_view.show()
        #self.close()

    def login(self):
        mail = self.username.text()
        password = self.password.text()

        # if mail == "" or password == "":
        #     QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
        #                          QMessageBox.Ok, QMessageBox.Ok)
        # else:
        # TODO: uncomment check
        # mail = 'edopant@gmail.com'  # 'mariorossi@gmail.com'
        # password = 'ciao'
        if mail != '' and password != '':
            check, person = self.can_login(mail, password)
            if check:
                self.hide()
                self.go_home = HomeView.HomeView(person)
                self.go_home.show()
                self.close()

            else:
                messageBox = QMessageBox()
                messageBox.critical(messageBox, 'Errore', 'Controlla Mail e Password',
                                    messageBox.Ok, messageBox.Ok)
        else:
            messageBox = QMessageBox()
            messageBox.critical(messageBox, 'Errore', 'Riempi i campi Mail e Password',
                                messageBox.Ok, messageBox.Ok)

    def can_login(self, mail, password):
        with open("Classes/Person/users.txt", 'r') as f:
            for person in json.load(f):
                if person['mail'] == mail and person['password'] == password:
                    if person['job'] == 0:
                        customer = Customer(person['id'],
                                            person['name'],
                                            person['surname'],
                                            person['mail'],
                                            person['password'],
                                            person['date_of_birth'],
                                            person['place_of_birth'],
                                            person['phone_number'],
                                            person['address'],
                                            0,
                                            person['payment_method'],
                                            person['credit_card_number'],
                                            person['permissions'],
                                            person['valid_trough'],
                                            person['ccv'],
                                            person['iban'])
                        return True, customer
                    elif person['job'] == 1:
                        employee = Employee(person['id'],
                                            person['name'],
                                            person['surname'],
                                            person['mail'],
                                            person['password'],
                                            person['date_of_birth'],
                                            person['place_of_birth'],
                                            person['phone_number'],
                                            person['address'],
                                            1,
                                            person['role'],
                                            person['salary'],
                                            person['permissions'],
                                            person['hire_date'])
                        return True, employee
                    else:
                        person = Person(person['id'],
                                        person['name'],
                                        person['surname'],
                                        person['mail'],
                                        person['password'],
                                        person['date_of_birth'],
                                        person['place_of_birth'],
                                        person['phone_number'],
                                        person['address'],
                                        2)
                        return True, person
            f.close()
            return False, Person('', '', '', '', '', '', '', '', '', 0)

