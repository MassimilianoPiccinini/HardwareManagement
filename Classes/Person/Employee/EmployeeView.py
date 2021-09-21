from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Person.Employee.EmployeeController import EmployeeController
from Classes.Person.EmployeesList.EmployeesListController import EmployeesListController


class EmployeeView(QWidget):
    def __init__(self, employee, user, index, list_controller, parent=None):
        super(EmployeeView, self).__init__(parent)
        self.controller = EmployeeController(employee)
        self.list_controller = list_controller
        self.employee = employee
        self.index = index

        is_enabled = user.job == 2

        self.info = {}
        self.stylesheet = """QPushButton{border-radius: 15px; background-color: #228B22;color: white;}"""
        self.resize(550, 550)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni del nuovo dipendente.

        self.create_label("Nome", 50, 40)
        self.name = self.create_info_label(self.controller.get_name(), is_enabled, False, False)
        self.name.setGeometry(50, 70, 200, 30)

        self.create_label("Cognome", 50, 110)
        self.surname = self.create_info_label(self.controller.get_surname(), is_enabled, False, False)
        self.surname.setGeometry(50, 140, 200, 30)

        self.create_label("email", 50, 180)
        self.email = self.create_info_label(self.controller.get_mail(), is_enabled, False, False)
        self.email.setGeometry(50, 210, 200, 30)

        self.create_label("Data di Nascita", 50, 250)
        day = int(self.controller.get_date_of_birth()[0] + self.controller.get_date_of_birth()[1])
        month = int(self.controller.get_date_of_birth()[3] + self.controller.get_date_of_birth()[4])
        year = int(self.controller.get_date_of_birth()[6] + self.controller.get_date_of_birth()[7] +
                   self.controller.get_date_of_birth()[8] + self.controller.get_date_of_birth()[9])
        self.date_of_birth = self.create_info_label('', is_enabled, True, False, QDate(year, month, day))
        self.date_of_birth.setGeometry(50, 280, 200, 30)

        self.create_label("Luogo di Nascita", 50, 320)
        self.place_of_birth = self.create_info_label(self.controller.get_place_of_birth(), is_enabled, False, False)
        self.place_of_birth.setGeometry(50, 350, 200, 30)

        self.create_label("Numero di Telefono", 50, 390)
        self.phone_number = self.create_info_label(self.controller.get_phone_number(), is_enabled, False, False)
        self.phone_number.setGeometry(50, 420, 200, 30)

        self.create_label("Indirizzo", 300, 40)
        self.address = self.create_info_label(self.controller.get_address(), is_enabled, False, False)
        self.address.setGeometry(300, 70, 200, 30)

        self.create_label('Ruolo', 300, 110)
        self.role = self.create_info_label(self.controller.get_role(), is_enabled, False, False)
        self.role.setGeometry(300, 140, 200, 30)

        self.create_label('Salario', 300, 180)
        self.salary = self.create_info_label(self.controller.get_salary(), is_enabled, False, False)
        self.salary.setGeometry(300, 210, 200, 30)

        self.create_label('Permessi', 300, 250)
        self.permissions = self.create_info_label(self.controller.get_permissions(), is_enabled, False, False)
        self.permissions.setGeometry(300, 280, 200, 30)

        self.create_label('Data di Assunzione', 300, 320)
        day = int(self.controller.get_hire_date()[0] + self.controller.get_hire_date()[1])
        month = int(self.controller.get_hire_date()[3] + self.controller.get_hire_date()[4])
        year = int(self.controller.get_hire_date()[6] + self.controller.get_hire_date()[7] +
                   self.controller.get_hire_date()[8] + self.controller.get_hire_date()[9])
        self.hire_date = self.create_info_label('', False, True, False, QDate(year, month, day))
        self.hire_date.setGeometry(300, 350, 200, 30)

        if is_enabled:
            self.update_button = self.create_button('Salva Modifiche')
            self.update_button.clicked.connect(self.update_employee_click)
            self.update_button.setGeometry(340, 385, 120, 35)

            self.delete_button = self.create_button('Elimina Dipendente')
            self.delete_button.clicked.connect(self.delete_employee_click)
            self.delete_button.setGeometry(340, 425, 120, 35)

        self.setWindowTitle(self.controller.get_name() + ' ' + self.controller.get_surname())

    def update_employee_click(self):
        self.controller.set_name(self.name.text())
        self.controller.set_surname(self.surname.text())
        self.controller.set_mail(self.email.text())
        self.controller.set_date_of_birth(self.date_of_birth.text())
        self.controller.set_place_of_birth(self.place_of_birth.text())
        self.controller.set_phone_number(self.phone_number.text())
        self.controller.set_address(self.address.text())
        self.controller.set_role(self.role.text())
        self.controller.set_salary(self.salary.text())
        self.controller.set_permissions(self.permissions.text())
        self.controller.set_hire_date(self.hire_date.text())
        self.list_controller.update_employee_by_index(self.index, self.employee.id_person, self.name.text(),
                                                      self.surname.text(), self.email.text(),
                                                      self.employee.password, self.date_of_birth.text(),
                                                      self.place_of_birth.text(), self.phone_number.text(),
                                                      self.address.text(), 1, self.role.text(), self.salary.text(),
                                                      self.permissions.text(), self.hire_date.text())
        self.close()

    def delete_employee_click(self):
        self.list_controller.delete_employee_by_index(self.index)
        self.close()

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
