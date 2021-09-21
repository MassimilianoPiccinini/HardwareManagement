from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Classes.Person.EmployeesList.EmployeesListView import EmployeesListView
from Classes.Person.CustomersList.CustomersListView import CustomersListView
from Classes.ProductsList.ProductsListView import ProductsListView
from Classes.Home.TransactionsView import TransactionsView
from Classes.Transactions.SalesList.SalesListView import SalesListView
from Classes.Person.PersonView import PersonView
from Classes.Home.AssistanceView import AssistanceView


class HomeView(QWidget):

    def __init__(self, user, parent=None):
        super(HomeView, self).__init__(parent)

        self.employees_list_view = EmployeesListView(user)
        self.customers_list_view = CustomersListView(user)
        self.products_list_view = ProductsListView(user)
        self.person_view = PersonView(user)
        self.sales_view = SalesListView(user)
        self.assistance_view = AssistanceView()
        self.user = user

        image_path = "Images/FerramentaBertiSfondo.jpg"
        image = QImage(image_path)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)
        self.label.setGraphicsEffect(opacity_effect)
        self.label.setGeometry(0, 0, 0, 0)
        self.label.setFixedSize(self.size().width() * 2, self.size().height() * 2)

        grid_layout = QGridLayout()

        me_button = self.get_generic_button('I miei Dati', self.go_my_info, 'user_logo',
                                                  '#00919b')
        grid_layout.addWidget(me_button, 0, 0)

        products_button = self.get_generic_button('Prodotti', self.go_products_list, 'products_logo',
                                                  'blue')
        grid_layout.addWidget(products_button, 0, 1)
        if user.job > 0:
            transactions_button = self.get_generic_button('Transazioni', self.go_transactions_list, 'transactions_logo',
                                                          'lightgreen')
            grid_layout.addWidget(transactions_button, 1, 0)
            grid_layout.addWidget(self.get_generic_button("Clienti", self.go_customers_list, 'customers_logo',
                                                          'red'), 1, 1)
            grid_layout.addWidget(self.get_generic_button("Dipendenti", self.go_employees_list, 'employees_logo',
                                                          'orange'), 0, 2)
            grid_layout.addWidget(self.get_generic_button("Assistenza", self.go_assistance, 'phone_logo',
                                                          '#FFD479'), 1, 2)
        else:
            sales_button = self.get_generic_button('Acquista', self.go_sales_list, 'transactions_logo',
                                                          'lightgreen')
            grid_layout.addWidget(sales_button, 1, 0)
            grid_layout.addWidget(self.get_generic_button("Assistenza", self.go_assistance, 'phone_logo',
                                                          '#FFD479'), 1, 1)

        self.buttons_grid = QLabel(self)
        self.buttons_grid.setLayout(grid_layout)
        self.showMaximized()
        self.buttons_grid.setGeometry((self.size().width() - 650) / 2, (self.size().height() - 390) / 2, 650, 390)
        self.setWindowTitle("Gestionale Ferramenta Berti")

    def get_generic_label(self, title):
        label = QLabel(title)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont('Helvetica', 18, QFont.Bold)
        label.setFont(font)

        return label

    def get_generic_button(self, title, on_click, image_path, main_color):
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont('Helvetica', 28, QFont.Bold)
        button.setFont(font)
        button.clicked.connect(on_click)

        button.setText(title)
        button.setIcon(QIcon('Images/' + image_path + '.png'))
        button.setIconSize(QSize(50, 50))

        button.setStyleSheet('QToolButton{'
                             'background-repeat: no-repeat; background-position: center; '
                             'border-radius: 16px; color: ' + main_color + '; border-radius: 30px;'
                                                                           'background-color: white; border-width: 2px; border-style: solid; '
                                                                           'border-color: white;}'
                                                                           'QToolButton::Hover{border-color: ' + main_color + ';}')
        return button

    def go_products_list(self):
        self.products_list_view.show()

    def go_customers_list(self):
        self.customers_list_view.show()

    def go_employees_list(self):
        self.employees_list_view.show()

    def go_transactions_list(self):
        self.transactions_view = TransactionsView(self.user)
        self.transactions_view.show()
        self.transactions_view.raise_()

    def go_sales_list(self):
        self.sales_view.show()
        self.sales_view.raise_()

    def go_my_info(self):
        self.person_view.show()

    def go_assistance(self):
        self.assistance_view.show()


