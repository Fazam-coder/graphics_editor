from Figure import Figure


class Line(Figure):
    def __init__(self, sx, sy, ex, ey):
        super().__init__(sx, sy)
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        super().draw(painter)
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)