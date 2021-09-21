from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QDateEdit

from Classes.Person.Employee import EmployeeController


class AddEmployeeView(QWidget):
    def __init__(self, controller, user, callback):
        super(AddEmployeeView, self).__init__()
        self.controller = controller
        self.callback = callback
        is_enabled = user.job == 2

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 550)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni del nuovo dipendente.

        self.create_label("Nome", 50, 40)
        self.name = self.create_info_label(is_enabled, False, False)
        self.name.setGeometry(50, 70, 200, 30)

        self.create_label("Cognome", 50, 110)
        self.surname = self.create_info_label(is_enabled, False, False)
        self.surname.setGeometry(50, 140, 200, 30)

        self.create_label("email", 50, 180)
        self.email = self.create_info_label(is_enabled, False, False)
        self.email.setGeometry(50, 210, 200, 30)

        self.create_label("password", 50, 250)
        self.password = self.create_info_label(is_enabled, False, True)
        self.password.setGeometry(50, 280, 200, 30)

        self.create_label("Data di Nascita", 50, 320)
        self.date_of_birth = self.create_info_label(is_enabled, True, False)
        self.date_of_birth.setGeometry(50, 350, 200, 30)

        self.create_label("Luogo di Nascita", 50, 390)
        self.place_of_birth = self.create_info_label(is_enabled, False, False)
        self.place_of_birth.setGeometry(50, 420, 200, 30)

        self.create_label("Numero di Telefono", 300, 40)
        self.phone_number = self.create_info_label(is_enabled, False, False)
        self.phone_number.setGeometry(300, 70, 200, 30)

        self.create_label("Indirizzo", 300, 110)
        self.address = self.create_info_label(is_enabled, False, False)
        self.address.setGeometry(300, 140, 200, 30)

        self.create_label('Ruolo', 300, 180)
        self.role = self.create_info_label(is_enabled, False, False)
        self.role.setGeometry(300, 210, 200, 30)

        self.create_label('Salario', 300, 250)
        self.salary = self.create_info_label(is_enabled, False, False)
        self.salary.setGeometry(300, 280, 200, 30)

        self.create_label('Permessi', 300, 320)
        self.permissions = self.create_info_label(is_enabled, False, False)
        self.permissions.setGeometry(300, 350, 200, 30)

        self.create_label('Data di Assunzione', 300, 390)
        self.hire_date = self.create_info_label(is_enabled, True, False)
        self.hire_date.setGeometry(300, 420, 200, 30)

        if is_enabled:

            self.create_button = self.create_button('Crea Dipendente')
            self.create_button.clicked.connect(self.add_employee_click)
            self.create_button.setGeometry(215, 475, 120, 35)

        self.setWindowTitle("Nuovo Dipendente")

    def create_label(self, name, x, y):
        label_edit = QLabel(self)
        label_edit.setText(name)
        label_edit.setGeometry(x + 10, y, 150, 30)
        font_label = QFont("Helvetica", 12, QFont.Bold)
        label_edit.setFont(font_label)

    def create_info_label(self, is_enabled, is_date, is_password):
        if is_date:
            info_label = QDateEdit(self)
            info_label.setDisplayFormat("dd/MM/yyyy")
            info_label.setEnabled(is_enabled)
            font = QFont("Helvetica", 12, QFont.Bold)
            info_label.setFont(font)
            info_label.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px;')
            return info_label
        else:
            info_label = QLineEdit(self)
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

    def add_employee_click(self):
        name = self.name.text().strip()
        surname = self.surname.text().strip()
        email = self.email.text().strip().lower()
        password = self.password.text().strip()
        date_of_birth = self.date_of_birth.text().strip()
        place_of_birth = self.place_of_birth.text().strip()
        phone_number = self.phone_number.text().strip()
        address = self.address.text().strip()
        role = self.role.text().strip()
        salary = self.salary.text().strip()
        permissions = self.permissions.text().strip()
        hire_date = self.hire_date.text().strip()

        if name == "" or surname == "" or email == "" or password == "" or date_of_birth == "" or place_of_birth == "" \
                or phone_number == "" or address == "" or role == "" or salary == "" or permissions == "" or \
                hire_date == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.create_employee(name, surname, email, password, date_of_birth,
                                            place_of_birth, phone_number, address, 1, role, salary, permissions, hire_date)
            self.callback()
            self.close()
