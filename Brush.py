from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPen

from Figure import Figure
from const import COLOR, THIKNESS


class Brush(Figure):
    def __init__(self, sx, sy, ex, ey):
        super().__init__(sx, sy)
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        super().draw(painter)
        painter.setPen(QPen(COLOR, THIKNESS))
        painter.drawLine(QPoint(self.sx, self.sy), QPoint(self.ex, self.ey))