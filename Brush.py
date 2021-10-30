from PyQt5.QtGui import QColor

from Figure import Figure
from const import COLOR, THIKNESS

# Опасен, изменяет painter


class Brush(Figure):
    def __init__(self, sx, sy):
        super().__init__(sx, sy)

    def draw(self, painter):
        super().draw(painter)
        painter.setBrush(COLOR)
        painter.drawEllipse(self.sx - THIKNESS // 2, self.sy - THIKNESS // 2, THIKNESS, THIKNESS)
        painter.setBrush(QColor(255, 255, 255))