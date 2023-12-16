import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic.properties import QtCore, QtWidgets

from circle import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button = QPushButton('Создать окружность', self)
        self.button.clicked.connect(self.create_circle)

        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setBrush(color)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(circle['x'], circle['y'], circle['diameter'], circle['diameter'])

    def create_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        self.circles.append({'x': x, 'y': y, 'diameter': diameter})
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 500, 500)
    window.show()
    sys.exit(app.exec_())