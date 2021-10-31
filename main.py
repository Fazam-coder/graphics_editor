import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from Canvas import Canvas
from const import COLOR
from AboutProgram import AboutProgram


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        self.setCentralWidget(Canvas())
        self.action_brush.triggered.connect(self.centralWidget().set_brush)
        self.action_line.triggered.connect(self.centralWidget().set_line)
        self.action_circle.triggered.connect(self.centralWidget().set_circle)
        self.action_rectangle.triggered.connect(self.centralWidget().set_rectangle)
        self.action_color.triggered.connect(self.set_color)
        self.action_eraser.triggered.connect(self.centralWidget().set_eraser)
        self.action_program.triggered.connect(self.about_program)

    def set_color(self):
        pass

    def set_thikness(self):
        pass

    def about_program(self):
        self.program = AboutProgram(self)
        self.program.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())