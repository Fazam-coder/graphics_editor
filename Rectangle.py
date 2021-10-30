from Figure import Figure


class Rectangle(Figure):
    def __init__(self, sx, sy, ex, ey):
        super().__init__(sx, sy)
        self.ex = ex
        self.ey = ey

    def draw(self, painter):
        super().draw(painter)
        painter.drawRect(min(self.sx, self.ex), min(self.sy, self.ey),
                         abs(self.sx - self.ex), abs(self.sy - self.ey))