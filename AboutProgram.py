from PyQt5.QtWidgets import QWidget

from ui_about_program import Ui_Form


class AboutProgram(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open('about_program.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            self.text_program.setText(data)