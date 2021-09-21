from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Classes.Person.EmployeesList.EmployeesListController import EmployeesListController
from Classes.Person.Employee.AddEmployeeView import AddEmployeeView
from Classes.Person.Employee.EmployeeView import EmployeeView


class EmployeesListView(QWidget):

    def __init__(self, user, parent=None):
        super(EmployeesListView, self).__init__(parent)
        self.controller = EmployeesListController()
        self.controller.model.get_employees_list()
        self.user = user
        self.add_employee_view = AddEmployeeView(self.controller, self.user, self.update_ui)

        is_enabled = user.job == 2

        image_path = "Images/employees_list_background.jpg"
        image = QImage(image_path)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)
        self.label.setGraphicsEffect(opacity_effect)
        self.label.setGeometry(0, 0, 600, 300)
        self.label.setFixedSize(self.size())

        self.table_view = QTableView(self)
        self.update_ui()

        open_button = QToolButton(self)
        open_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        font_button = QFont("Helvetica", 11)
        open_button.setFont(font_button)
        open_button.setGeometry(460, 10, 120, 70)
        open_button.setIcon(QIcon('Images/lens.png'))
        open_button.setText("Visualizza Informazioni")
        open_button.setIconSize(QSize(50, 50))
        open_button.clicked.connect(self.show_selected_info)
        open_button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; '
                                  'border-radius: 10px;}'
                                  'QToolButton::Hover{background-color: #00afff}')

        if is_enabled:
            new_button = QToolButton(self)
            new_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            font_button = QFont("Helvetica", 11)
            new_button.setFont(font_button)
            new_button.setGeometry(460, 100, 120, 70)
            new_button.setIcon(QIcon('Images/new_user.png'))
            new_button.setText("Aggiungi Dipendente")
            new_button.setIconSize(QSize(50, 50))
            new_button.clicked.connect(self.show_new_employee)
            new_button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; '
                                     'border-radius: 10px;}'
                                 'QToolButton::Hover{background-color: #00afff}')

        self.resize(600, 300)
        self.setWindowTitle('Lista Dipendenti')

    def closeEvent(self, event):
        # self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected_index = self.table_view.currentIndex().row()
        selected_employee = self.controller.get_employee_by_index(selected_index)
        self.employee_view = EmployeeView(selected_employee, self.user, selected_index, self.controller)
        self.employee_view.show()

    def show_new_employee(self):
        self.add_employee_view.show()

    def update_ui(self):
        table_view_model = QStandardItemModel(self)

        table_view_model.setHorizontalHeaderLabels(['Dipendente', 'Mail', 'Data Assunzione'])
        self.table_view.setGeometry(10, 10, 440, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        for employee in self.controller.get_employees_list():
            name_surname_item = QStandardItem()
            name_surname = employee.name[0] + '.  ' + employee.surname
            name_surname_item.setText(name_surname)
            name_surname_item.setEditable(False)
            font = name_surname_item.font()
            font.setPointSize(13)
            name_surname_item.setFont(font)

            email_item = QStandardItem()
            email_item.setText(employee.mail)
            email_item.setEditable(False)
            font = email_item.font()
            font.setPointSize(13)
            email_item.setFont(font)

            hire_date_item = QStandardItem()
            hire_date_item.setText(employee.hire_date)
            hire_date_item.setEditable(False)
            font = hire_date_item.font()
            font.setPointSize(13)
            hire_date_item.setFont(font)

            table_view_model.appendRow([name_surname_item, email_item, hire_date_item])
        self.table_view.setModel(table_view_model)
        self.table_view.setColumnWidth(0, int(self.table_view.width() / 3 - 5))
        self.table_view.setColumnWidth(1, int(self.table_view.width() / 3 - 5))
        self.table_view.setColumnWidth(2, int(self.table_view.width() / 3 - 5))
