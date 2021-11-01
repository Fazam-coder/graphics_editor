from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QGradient

from const import *


class Figure:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        painter.setPen(QPen(COLOR, THIKNESS))