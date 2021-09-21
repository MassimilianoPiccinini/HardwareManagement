from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Classes.Transactions.SalesList.SalesListView import SalesListView
from Classes.Transactions.OrdersList.OrdersListView import OrdersListView


class TransactionsView(QWidget):

    def __init__(self, user, parent=None):
        super(TransactionsView, self).__init__(parent)

        self.sales_list_view = SalesListView(user)
        self.orders_list_view = OrdersListView(user)

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

        products_button = self.get_generic_button('Vendite', self.go_sales_list, 'cashDesk_logo',
                                                  '000000')
        grid_layout.addWidget(products_button, 0, 0)
        if user.job > 0:
            transactions_button = self.get_generic_button('Ordini', self.go_orders_list, 'camion_logo',
                                                          '919191')
            grid_layout.addWidget(transactions_button, 0, 1)

        self.buttons_grid = QLabel(self)
        self.buttons_grid.setLayout(grid_layout)
        self.showMaximized()
        self.buttons_grid.setGeometry((self.size().width() - 600) / 2, (self.size().height() - 300) / 2, 600, 300)
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
        button.setIconSize(QSize(100, 100))

        button.setStyleSheet('QToolButton{'
                             'background-repeat: no-repeat; background-position: center; '
                             'border-radius: 16px; color: #' + main_color + '; border-radius: 30px;'
                             'background-color: white; border-width: 2px; border-style: solid; '
                             'border-color: white;}'
                             'QToolButton::Hover{border-color: #' + main_color + ';}')
        return button

    def go_sales_list(self):
        self.sales_list_view.show()

    def go_orders_list(self):
        self.orders_list_view.show()
