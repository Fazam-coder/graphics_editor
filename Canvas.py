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
        self.instrument = 'b'

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y()))
        elif self.instrument == 'l':
            self.objects.append(Line(event.x(), event.y(), event.x(), event.y()))
        elif self.instrument == 'r':
            self.objects.append(Rectangle(event.x(), event.y(), event.x(), event.y()))
        elif self.instrument == 'c':
            self.objects.append(Circle(event.x(), event.y(), event.x(), event.y()))
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y()))
        self.update()

    def mouseMoveEvent(self, event):
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y()))
        elif self.instrument == 'l' or self.instrument == 'r' or self.instrument == 'c':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y()))
        self.update()

    def set_brush(self):
        self.instrument = 'b'

    def set_circle(self):
        self.instrument = 'c'

    def set_line(self):
        self.instrument = 'l'

    def set_rectangle(self):
        self.instrument = 'r'

    def set_eraser(self):
        self.instrument = 'e'