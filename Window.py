from PyQt5.QtWidgets import QMainWindow

from Canvas import Canvas
from AboutProgram import AboutProgram
from ui_window import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCentralWidget(Canvas())
        self.initUI()

    def initUI(self):
        self.action_brush.triggered.connect(self.centralWidget().set_brush)
        self.action_line.triggered.connect(self.centralWidget().set_line)
        self.action_circle.triggered.connect(self.centralWidget().set_circle)
        self.action_rectangle.triggered.connect(self.centralWidget().set_rectangle)
        self.action_color.triggered.connect(self.centralWidget().set_color)
        self.action_eraser.triggered.connect(self.centralWidget().set_eraser)
        self.action_program.triggered.connect(self.about_program)
        self.action_thickness.triggered.connect(self.centralWidget().set_thickness)
        self.action_back.triggered.connect(self.centralWidget().back)
        self.action_forward.triggered.connect(self.centralWidget().forward)

    def about_program(self):
        self.program = AboutProgram()
        self.program.show()