from PyQt5.QtGui import QPen


class Figure:
    def __init__(self, sx, sy, ex, ey, color, thikness):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color = color
        self.thikness = thikness

    def draw(self, painter):
        painter.setPen(QPen(self.color, self.thikness))