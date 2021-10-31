from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AboutProgram(QWidget):
    def __init__(self, arg):
        super().__init__()
        uic.loadUi('about_program.ui', self)
        with open('about_program.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            self.text_program.setText(data)