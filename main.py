import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class PayForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())