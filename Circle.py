from Figure import Figure


class Circle(Figure):
    def draw(self, painter):
        super().draw(painter)
        painter.drawEllipse(min(self.sx, self.ex), min(self.sy, self.ey),
                            abs(self.sx - self.ex), abs(self.sy - self.ey))