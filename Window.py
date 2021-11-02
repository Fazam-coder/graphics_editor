from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from Canvas import Canvas
from AboutProgram import AboutProgram


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        self.setCentralWidget(Canvas())
        self.initUI()

    def initUI(self):
        # self.lbl_image = QLabel()
        # self.lbl_image.resize(self.x(), self.y())
        # self.lbl_image.move(0, 0)
        self.action_brush.triggered.connect(self.centralWidget().set_brush)
        self.action_line.triggered.connect(self.centralWidget().set_line)
        self.action_circle.triggered.connect(self.centralWidget().set_circle)
        self.action_rectangle.triggered.connect(self.centralWidget().set_rectangle)
        self.action_color.triggered.connect(self.centralWidget().set_color)
        self.action_eraser.triggered.connect(self.centralWidget().set_eraser)
        self.action_program.triggered.connect(self.about_program)
        self.action_open.triggered.connect(self.centralWidget().open_image)

    def about_program(self):
        self.program = AboutProgram()
        self.program.show()

    # def open_image(self):
    #     self.lbl_image = QLabel(self)
    #     self.lbl_image.resize(self.size())
    #     self.lbl_image.move(0, 0)
    #     fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
    #     self.pixmap = QPixmap(fname)
    #     self.lbl_image.setPixmap(self.pixmap)