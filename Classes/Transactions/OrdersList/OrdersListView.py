from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.Transactions.OrdersList.OrdersListController import OrdersListController
from Classes.Transactions.Order.AddOrderView import AddOrderView
from Classes.Transactions.Order.OrderView import OrderView
from Classes.ProductsList.ProductsListController import ProductsListController


class OrdersListView(QWidget):

    def __init__(self, user, parent=None):
        super(OrdersListView, self).__init__(parent)
        self.controller = OrdersListController()
        self.controller.model.get_orders_list()
        self.products_list_controller = ProductsListController()
        self.products_list_controller.get_products_list()
        self.user = user
        self.add_order_view = AddOrderView(self.controller, self.user, self.update_ui)

        is_enabled = user.job == 2

        image_path = "Images/orders_list_background.jpg"
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
            new_button.setText("Nuovo Ordine")
            new_button.setIconSize(QSize(50, 50))
            new_button.clicked.connect(self.show_new_order)
            new_button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; '
                                     'border-radius: 10px;}'
                                     'QToolButton::Hover{background-color: #00afff}')

        self.resize(600, 300)
        self.setWindowTitle('Lista Ordini')

    def closeEvent(self, event):
        # self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected_index = self.table_view.currentIndex().row()
        selected_order = self.controller.get_order_by_index(selected_index)
        self.order_view = OrderView(selected_order, self.user, selected_index, self.controller, self.update_ui)
        self.order_view.show()

    def show_new_order(self):
        self.add_order_view.show()

    def update_ui(self):
        table_view_model = QStandardItemModel(self)
        for order in self.controller.model.get_orders_list():
            product = self.products_list_controller.get_product_by_id(order.id_product)

            product_item = QStandardItem()
            product_item.setText(str(product.name))
            product_item.setEditable(False)
            font = product_item.font()
            font.setPointSize(13)
            product_item.setFont(font)

            quantity_item = QStandardItem()
            quantity_item.setText(str(order.quantity))
            quantity_item.setEditable(False)
            font = quantity_item.font()
            font.setPointSize(13)
            quantity_item.setFont(font)

            date_item = QStandardItem()
            date_item.setText(str(order.date))
            date_item.setEditable(False)
            font = date_item.font()
            font.setPointSize(13)
            date_item.setFont(font)

            amount_item = QStandardItem()
            amount_item.setText("€ " + str(int(int(product.price) * int(order.quantity))))
            amount_item.setEditable(False)
            font = amount_item.font()
            font.setPointSize(13)
            amount_item.setFont(font)

            table_view_model.appendRow([product_item, quantity_item, date_item, amount_item])
        self.table_view.setModel(table_view_model)
        table_view_model.setHorizontalHeaderLabels(['Prodotto', 'Quantità', 'Data', 'Importo'])
        self.table_view.setGeometry(10, 10, 440, 280)
        self.table_view.setStyleSheet('border-radius: 10px')

        self.table_view.setColumnWidth(0, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(1, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(2, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(3, int(self.table_view.width() / 4 - 5))

