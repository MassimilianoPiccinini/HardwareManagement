from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AssistanceView(QWidget):

    def __init__(self, parent=None):
        super(AssistanceView, self).__init__(parent)

        self.movieView = QLabel(self)
        movie = QMovie("Images/Running_Man.gif")
        self.movieView.setMovie(movie)
        self.movieView.setGeometry(0, 0, 800, 600)
        movie.setSpeed(150)
        movie.start()

        self.label = QLabel(self)
        self.label.setText("La preghiamo di attendere,  un assistente sarà subito a sua disposizione")
        self.label.setStyleSheet("font-weight: bold; text-align: center; font-size: 20px")
        self.label.setGeometry(50, 600, 700, 50)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("background-color: white;")
        self.setFixedSize(800, 700)

