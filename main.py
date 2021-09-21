import sys
from PyQt5.QtWidgets import QApplication

from Classes.Home.LoginView import LoginView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_view = LoginView()
    login_view.show()
    sys.exit(app.exec())
