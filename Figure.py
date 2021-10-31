from PyQt5.QtGui import QColor, QPen

from const import *


class Figure:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        painter.setPen(COLOR)
        pen = QPen()
        pen.setWidth(THIKNESS)
        painter.setPen(pen)