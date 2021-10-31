from Figure import Figure


class Line(Figure):
    def draw(self, painter):
        super().draw(painter)
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)