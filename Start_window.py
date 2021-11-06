from PyQt5.QtWidgets import QWidget

from query_db import delete_all, select_all
from const import LOG
from Window import Window
from ui_start import Ui_Form


class Start_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if select_all():
            self.show()
        else:
            self.run_window()
        self.btn_ok.clicked.connect(self.run_window)

    def run_window(self):
        if self.radio_btn_no.isChecked():
            delete_all(LOG)
        self.window = Window()
        self.window.show()
        self.close()

    def closeEvent(self, event):
        self.run_window()