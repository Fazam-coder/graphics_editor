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
        self.add_paint_1()

    # добавление в self.objects елементов из БД
    def add_paint_1(self):
        for object in select_all():
            obj = object[NUM_ACTION]
            sx = object[NUM_SX]
            sy = object[NUM_SY]
            ex = object[NUM_EX]
            ey = object[NUM_EY]
            clr = QColor(object[NUM_RED], object[NUM_GREEN], object[NUM_BLUE])
            thick = object[NUM_THICKNESS]
            self.add_paint_2(obj, sx, sy, ex, ey, clr, thick)

    def add_paint_2(self, obj, sx, sy, ex, ey, clr, thick):
        if select_action(obj) == 'Brush':
            self.objects.append(Brush(sx, sy, ex, ey, clr, thick))
        elif select_action(obj) == 'Line':
            self.objects.append(Line(sx, sy, ex, ey, clr, thick))
        elif select_action(obj) == 'Rectangle':
            self.objects.append(Rectangle(sx, sy, ex, ey, clr, thick))
        elif select_action(obj) == 'Circle':
            self.objects.append(Circle(sx, sy, ex, ey, clr, thick))
        elif select_action(obj) == 'Eraser':
            self.objects.append(Eraser(sx, sy, ex, ey, clr, thick))
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            if obj:
                obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event):
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y(), color, thickness))
            self.add_in_db()
        elif self.instrument == 'l':
            self.objects.append(Line(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'r':
            self.objects.append(Rectangle(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'c':
            self.objects.append(Circle(event.x(), event.y(), event.x(), event.y(), color, thickness))
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y(), color, thickness))
            self.add_in_db()
        self.objects_del.clear()
        self.update()

    def mouseMoveEvent(self, event):
        if self.instrument == 'b':
            self.objects.append(Brush(event.x(), event.y(), event.x(), event.y(), color, thickness))
            self.add_in_db()
        elif self.instrument == 'l' or self.instrument == 'r' or self.instrument == 'c':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
        elif self.instrument == 'e':
            self.objects.append(Eraser(event.x(), event.y(), event.x(), event.y(), color, thickness))
            self.add_in_db()
        self.update()

    def mouseReleaseEvent(self, event):
        self.add_in_db()
        self.objects.append('')

    def plus_id(self):
        global id, max_id
        id += 1
        # max_id может увеличиться больше, чем на 1, если мы в БД переместились назад больше чем на один
        max_id += max_id - id + 1

    def add_in_db(self):
        id_act = 1
        if self.instrument == 'b':
            id_act = select_id(ACTIONS, ACTION, BRUSH)
        elif self.instrument == 'l':
            id_act = select_id(ACTIONS, ACTION, LINE)
        elif self.instrument == 'c':
            id_act = select_id(ACTIONS, ACTION, CIRCLE)
        elif self.instrument == 'r':
            id_act = select_id(ACTIONS, ACTION, RECTANGLE)
        elif self.instrument == 'e':
            id_act = select_id(ACTIONS, ACTION, ERASER)
        self.plus_id()
        add_object(LOG, id, id_act, self.objects[-1].sx, self.objects[-1].sy,
                   self.objects[-1].ex, self.objects[-1].ey, color, thickness)

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

    def back(self):
        global id
        if self.objects:
            min_index = 0
            for index in range(len(self.objects) - 2, -1, -1):
                if not self.objects[index]:
                    break
                self.objects_del.append(self.objects[index])
                min_index = index
                id -= 1
            self.objects = self.objects[0:min_index]
            self.objects_del.append('')
        self.update()

    def forward(self):
        global id
        if self.objects_del:
            min_index = 0
            for index in range(len(self.objects_del) - 2, 0, -1):
                if not self.objects_del[index]:
                    break
                self.objects.append(self.objects_del[index])
                min_index = index
                id += 1
            self.objects_del = self.objects_del[0:min_index]
            self.objects.append('')
        self.update()