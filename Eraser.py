from PyQt5.QtCore import QRect, QPoint, QSize

from Figure import Figure
from const import THIKNESS


class Eraser(Figure):
    def draw(self, painter):
        super().draw(painter)
        r = QRect(QPoint(), THIKNESS * QSize())
        r.moveCenter(QPoint(self.ex, self.ey))
        painter.eraseRect(r)