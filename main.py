import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Canvas import Canvas
from const import COLOR


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        canvas = Canvas()
        canvas.setStyleSheet('background-color: #ffffff ')
        self.setCentralWidget(canvas)
        self.centralWidget().setStyleSheet('QWidget {background-color: #ffffff }')
        self.centralWidget().show()
        self.action_brush.triggered.connect(self.centralWidget().set_brush)
        self.action_line.triggered.connect(self.centralWidget().set_line)
        self.action_circle.triggered.connect(self.centralWidget().set_circle)
        self.action_rectangle.triggered.connect(self.centralWidget().set_rectangle)
        self.action_color.triggered.connect(self.set_color)

    def set_color(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())