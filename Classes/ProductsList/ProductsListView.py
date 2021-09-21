from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Classes.ProductsList.ProductsListController import ProductsListController
from Classes.Product.ProductView import ProductView


class ProductsListView(QWidget):

    def __init__(self, user, parent=None):
        super(ProductsListView, self).__init__(parent)
        self.controller = ProductsListController()
        self.controller.model.get_products_list()
        self.user = user

        image_path = "Images/products_list_background.jpg"
        image = QImage(image_path)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.5)
        self.label.setGraphicsEffect(opacity_effect)
        self.label.setGeometry(0, 10, 600, 300)
        self.label.setFixedSize(self.size())

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("cerca per nome prodotto")
        font = QFont("Helvetica", 12, QFont.Bold)
        self.search_bar.setFont(font)
        self.search_bar.setStyleSheet('padding-left: 10px; padding-right: 10px; border-radius: 8px; '
                                      'background-color: white')
        self.search_bar.textChanged.connect(self.on_change_text)
        self.search_bar.setGeometry(10, 10, 440, 30)

        self.table_view = QTableView(self)

        self.table_view.setGeometry(10, 60, 440, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        self.products_list = self.controller.model.products_list
        self.fill_data_in_table(self.products_list)

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

        # self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Prodotti')

    def fill_data_in_table(self, products_list):
        table_view_model = QStandardItemModel(self)
        table_view_model.setHorizontalHeaderLabels(['Prodotto', 'Prezzo', 'Quantità Disponibile'])
        for product in products_list:
            name_item = QStandardItem()
            name_item.setText(product.name)
            name_item.setEditable(False)
            font = name_item.font()
            font.setPointSize(13)
            name_item.setFont(font)

            price_item = QStandardItem()
            price_item.setText(product.price)
            price_item.setEditable(False)
            font = price_item.font()
            font.setPointSize(13)
            price_item.setFont(font)

            quantity_item = QStandardItem()
            quantity_item.setText(product.quantity)
            quantity_item.setEditable(False)
            font = quantity_item.font()
            font.setPointSize(13)
            quantity_item.setFont(font)

            table_view_model.appendRow([name_item, price_item, quantity_item])
        self.table_view.setModel(table_view_model)

    def closeEvent(self, event):
        # self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected_index = self.table_view.currentIndex().row()
        if selected_index == -1:
            QMessageBox.critical(self, 'Errore', 'Nessun prodotto selezionato', QMessageBox.Ok, QMessageBox.Ok)
        elif len(self.products_list) > selected_index:
            selected_product = self.products_list[selected_index]
            self.product_view = ProductView(selected_product, self.user, selected_index, self.controller)
            self.product_view.show()
        else:
            QMessageBox.critical(self, 'Errore', 'Nessun prodotto selezionato', QMessageBox.Ok, QMessageBox.Ok)

    def show_new_product(self):
        self.add_product_view.show()

    def on_change_text(self):
        self.products_list = self.controller.search_by_name(self.search_bar.text())
        self.fill_data_in_table(self.products_list)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self)
        self.table_view = QTableView(self)
        self.table_view.setGeometry(10, 10, 380, 280)
        self.table_view.setStyleSheet('border-radius: 10px')
        products_list = self.controller.model.products_list
        for product in products_list:
            item = QStandardItem()
            item.setText(product.name + ' ' + product.surname)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow([item, item])
        self.table_view.setModel(self.listview_model)
