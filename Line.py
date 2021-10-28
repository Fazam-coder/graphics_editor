from PyQt5.QtGui import QBrush, QColor


class Line:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color = (0, 0, 0)

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(self.color[0], self.color[1], self.color[2])))
        painter.setPen(QColor(self.color[0], self.color[1], self.color[2]))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)