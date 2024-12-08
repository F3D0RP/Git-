import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []  # Список для хранения окружностей

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
