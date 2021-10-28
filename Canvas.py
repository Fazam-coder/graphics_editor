from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from Brush import Brush
from Line import Line
from Rectangle import Rectangle
from Circle import Circle
from Eraser import Eraser


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for object in self.objects:
            object.draw(painter)
        painter.end()

    def mouseMoveEvent(self, event):
        self.objects.append(Brush(event.x(), event.y()))
        self.update()

    def mousePressEvent(self, event):
        self.objects.append(Brush(event.x(), event.y()))
        self.update()