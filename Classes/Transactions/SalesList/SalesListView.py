from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Classes.Transactions.SalesList.SalesListController import SalesListController
from Classes.Transactions.Sale.AddSaleView import AddSaleView
from Classes.Transactions.Sale.SaleView import SaleView
from Classes.ProductsList.ProductsListController import ProductsListController


class SalesListView(QWidget):

    def __init__(self, user, parent=None):
        super(SalesListView, self).__init__(parent)
        self.controller = SalesListController()
        self.products_list_controller = ProductsListController()
        self.products_list_controller.get_products_list()
        self.user = user
        self.add_sale_view = AddSaleView(self.controller, self.user, self.update_ui)

        is_enabled = user.job == 0
        self.is_enabled = is_enabled

        image_path = "Images/sales_list_background.jpg"
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
            new_button.setText("Nuovo Acquisto")
            new_button.setIconSize(QSize(50, 50))
            new_button.clicked.connect(self.show_new_sale)
            new_button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; '
                                     'border-radius: 10px;}'
                                     'QToolButton::Hover{background-color: #00afff}')

        self.resize(600, 300)

        if is_enabled:
            self.setWindowTitle('Lista Vendite')
        else:
            self.setWindowTitle('Lista Acquisti')

    def closeEvent(self, event):
        # self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected_index = self.table_view.currentIndex().row()
        if self.user.job > 0:
            selected_sale = self.controller.get_sale_by_index(selected_index)
            self.sale_view = SaleView(selected_sale, self.user, selected_index, self.controller, self.update_ui)
        else:
            selected_sale = self.controller.get_mine_sale_by_index(selected_index, self.user.id_person)
            self.sale_view = SaleView(selected_sale, self.user, selected_index, self.controller, self.update_ui)
        self.sale_view.show()

    def show_new_sale(self):
        self.add_sale_view.show()

    def update_ui(self):
        table_view_model = QStandardItemModel(self)

        table_view_model.setHorizontalHeaderLabels(['Prodotto', 'Quantità', 'Data', 'Importo'])
        self.table_view.setGeometry(10, 10, 440, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        if self.user.job == 0:
            sales_list = self.controller.model.get_mine_sales_list(self.user.id_person)
        else:
            sales_list = self.controller.model.get_sales_list()
        for sale in sales_list:
            product = self.products_list_controller.get_product_by_id(sale.id_product)

            product_item = QStandardItem()
            product_item.setText(str(product.name))
            product_item.setEditable(False)
            font = product_item.font()
            font.setPointSize(13)
            product_item.setFont(font)

            quantity_item = QStandardItem()
            quantity_item.setText(str(sale.quantity))
            quantity_item.setEditable(False)
            font = quantity_item.font()
            font.setPointSize(13)
            quantity_item.setFont(font)

            date_item = QStandardItem()
            date_item.setText(str(sale.date))
            date_item.setEditable(False)
            font = date_item.font()
            font.setPointSize(13)
            date_item.setFont(font)

            amount_item = QStandardItem()
            amount_item.setText("€ " + str(int(int(product.price) * int(sale.quantity))))
            amount_item.setEditable(False)
            font = amount_item.font()
            font.setPointSize(13)
            amount_item.setFont(font)

            table_view_model.appendRow([product_item, quantity_item, date_item, amount_item])
        self.table_view.setModel(table_view_model)
        self.table_view.setColumnWidth(0, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(1, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(2, int(self.table_view.width() / 4 - 5))
        self.table_view.setColumnWidth(3, int(self.table_view.width() / 4 - 5))

