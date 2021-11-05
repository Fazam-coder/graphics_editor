from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QColorDialog, QInputDialog

from Brush import Brush
from Line import Line
from Rectangle import Rectangle
from Circle import Circle
from Eraser import Eraser
from query_db import *
from const import *

color = QColor(0, 0, 0)
thickness = 5
id = 0
max_id = 0

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []
        self.objects_del = []
        self.instrument = 'b'

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            if obj:
                obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        global thickness
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'l':
            self.objects.append(Line(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'r':
            self.objects.append(Rectangle(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'c':
            self.objects.append(Circle(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y(), color, thickness))
        self.update()

    def mouseMoveEvent(self, event):
        global thickness
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'l' or self.instrument == 'r' or self.instrument == 'c':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y(), color, thickness))
        self.update()

    def mouseReleaseEvent(self, event):
        global id, max_id
        id += 1
        max_id += 1
        if self.instrument == 'b':
            add_object(LOG, id, select_id(ACTIONS, ACTION, BRUSH))
        elif self.instrument == 'l':
            add_object(LOG, id, select_id(ACTIONS, ACTION, LINE))
        elif self.instrument == 'c':
            add_object(LOG, id, select_id(ACTIONS, ACTION, CIRCLE))
        elif self.instrument == 'r':
            add_object(LOG, id, select_id(ACTIONS, ACTION, RECTANGLE))
        elif self.instrument == 'e':
            add_object(LOG, id, select_id(ACTIONS, ACTION, ERASER))
        self.objects.append('')

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

    def set_color(self):
        global color
        color = QColorDialog.getColor()

    def set_thickness(self):
        global thickness
        age, ok_pressed = QInputDialog.getInt(self, INPUT_THICKNESS, STR_THICKNESS,
                                              thickness, MIN_THICKNESS, MAX_THICKNESS)
        if ok_pressed:
            thickness = age

    def fill(self):
        pass