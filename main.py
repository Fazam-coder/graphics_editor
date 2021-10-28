import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Canvas import Canvas


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        self.setCentralWidget(Canvas())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())