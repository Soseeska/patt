import turtle #рисуем через черепашку


class Figure: #класс фигуры
    def __init__(self, name):
        self.name = name


class FigureSerializer:
    def serialize(self, name, side): #интерфейс
        serializer = self._get_serializer(side)
        return serializer(name)

    def _get_serializer(self,side): #фабрика отрисовки фигур
        if side == '1':
            return self._drawline_serialize
        elif side == '2':
            return self._drawangle_serialize
        elif side == '3':
            return self._drawtriangle_serialize
        elif side == '4':
            return self._drawsquare_serialize
        elif side == '5':
            return self._drawhecks_serialize
        else:
            raise ValueError(side)

    def _drawline_serialize(self, side): #отрисовка линии
        turtle.reset()
        turtle.down()
        turtle.forward(100)
        turtle.up()
        turtle.forward(100)
        turtle.mainloop()

    def _drawangle_serialize(self, side): #отрисовка угла
        turtle.reset()
        turtle.down()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.up()
        turtle.forward(100)
        turtle.mainloop()

    def _drawtriangle_serialize(self, side): #отрисовка треугольника
        turtle.reset()
        turtle.down()
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.up()
        turtle.forward(100)
        turtle.mainloop()

    def _drawsquare_serialize(self, side): #отрисовка квадрата
        turtle.reset()
        turtle.down()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.up()
        turtle.forward(100)
        turtle.mainloop()

    def _drawhecks_serialize(self, side): #отрисовка пятиугольника
        turtle.reset()
        turtle.down()
        turtle.forward(100)
        turtle.left(72)
        turtle.forward(100)
        turtle.left(72)
        turtle.forward(100)
        turtle.left(72)
        turtle.forward(100)
        turtle.left(72)
        turtle.forward(100)
        turtle.up()
        turtle.forward(100)
        turtle.mainloop()


figure_name = input('Введите наименование фигуры\n')
figure_size = input('Введите количество сторон\n')
figure = Figure(figure_name)
serializer = FigureSerializer()
serializer.serialize(figure, figure_size)
