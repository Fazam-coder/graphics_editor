from PyQt5.QtCore import QPoint

from Figure import Figure


class Brush(Figure):
    def draw(self, painter):
        super().draw(painter)
        painter.drawLine(QPoint(self.sx, self.sy), QPoint(self.ex, self.ey))