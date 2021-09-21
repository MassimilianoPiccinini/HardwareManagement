from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Person.Customer.CustomerView import CustomerView
from Classes.Person.CustomersList.CustomersListController import CustomersListController


class CustomersListView(QWidget):

    def __init__(self, user, parent=None):
        super(CustomersListView, self).__init__(parent)
        self.controller = CustomersListController()
        self.controller.model.get_customers_list()
        self.user = user
        # self.controller.__init__()

        image_path = "Images/customers_list_background.jpg"
        image = QImage(image_path)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)
        self.label.setGraphicsEffect(opacity_effect)
        self.label.setGeometry(0, 0, 600, 300)
        self.label.setFixedSize(self.size())
        table_view_model = QStandardItemModel(self)
        self.table_view = QTableView(self)

        table_view_model.setHorizontalHeaderLabels(['Cliente', 'Mail', 'Data di Nascita'])
        self.table_view.setGeometry(10, 10, 440, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        customers_list = self.controller.model.customers_list
        for customer in customers_list:
            name_surname_item = QStandardItem()
            name_surname = customer.name[0] + '.  ' + customer.surname
            name_surname_item.setText(name_surname)
            name_surname_item.setEditable(False)
            font = name_surname_item.font()
            font.setPointSize(13)
            name_surname_item.setFont(font)

            email_item = QStandardItem()
            email_item.setText(customer.mail)
            email_item.setEditable(False)
            font = email_item.font()
            font.setPointSize(13)
            email_item.setFont(font)

            date_of_birth_item = QStandardItem()
            date_of_birth_item.setText(customer.date_of_birth)
            date_of_birth_item.setEditable(False)
            font = date_of_birth_item.font()
            font.setPointSize(13)
            date_of_birth_item.setFont(font)

            table_view_model.appendRow([name_surname_item, email_item, date_of_birth_item])
        self.table_view.setModel(table_view_model)
        self.table_view.setColumnWidth(0, int(self.table_view.width() / 3 - 5))
        self.table_view.setColumnWidth(1, int(self.table_view.width() / 3 - 5))
        self.table_view.setColumnWidth(2, int(self.table_view.width() / 3 - 5))


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

        self.resize(600, 300)
        self.setWindowTitle('Lista Clienti')

    def closeEvent(self, event):
        # self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected_index = self.table_view.currentIndex().row()
        selected_customer = self.controller.get_customer_by_index(selected_index)
        self.customer_view = CustomerView(selected_customer, self.user, selected_index, self.controller)
        self.customer_view.show()

    def show_new_customer(self):
        self.add_customer_view.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self)
        self.table_view = QTableView(self)
        self.table_view.setGeometry(10, 10, 380, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        customers_list = self.controller.model.customers_list
        for customer in customers_list:
            item = QStandardItem()
            item.setText(customer.name + ' ' + customer.surname)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow([item, item])
        self.table_view.setModel(self.listview_model)
