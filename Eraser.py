from PyQt5.QtCore import QRect, QPoint, QSize

from Figure import Figure


class Eraser(Figure):
    def draw(self, painter):
        super().draw(painter)
        r = QRect(QPoint(), self.thikness * QSize())
        r.moveCenter(QPoint(self.ex, self.ey))
        painter.eraseRect(r)