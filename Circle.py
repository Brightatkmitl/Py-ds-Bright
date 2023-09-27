from shape import Shape


class Circle(Shape):
    def __init__(self, ray):
        self.cir_area = 0.0
        self.ray = ray
        self.pi = 3.14

    def area(self):
        self.cir_area = self.pi * self.ray * self.ray
        return self.cir_area

    def __str__(self) -> str:
        return ('Circle Area of '
                + str(self.ray) + 'Ux' + str(self.ray)
                + 'U :' + str(self.area()))
