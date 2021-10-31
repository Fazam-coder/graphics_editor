from PyQt5.QtCore import QRect, QPoint, QSize

from Figure import Figure
from const import THIKNESS


class Eraser(Figure):
    def __init__(self, sx, sy, ex, ey):
        super().__init__(sx, sy)
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        super().draw(painter)
        r = QRect(QPoint(), THIKNESS * QSize())
        r.moveCenter(QPoint(self.ex, self.ey))
        painter.eraseRect(r)