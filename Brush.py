from PyQt5.QtGui import QColor, QBrush


class Brush:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(self.color[0], self.color[1], self.color[2])))
        painter.setPen(QColor(self.color[0], self.color[1], self.color[2]))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)