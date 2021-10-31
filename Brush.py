from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPen

from Figure import Figure
from const import COLOR, THIKNESS


class Brush(Figure):
    def draw(self, painter):
        super().draw(painter)
        painter.setPen(QPen(COLOR, THIKNESS))
        painter.drawLine(QPoint(self.sx, self.sy), QPoint(self.ex, self.ey))