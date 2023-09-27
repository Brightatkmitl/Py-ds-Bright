from shape import Shape


class Triangle(Shape):
    def __init__(self, base,height):
        self.tri_area = 0.0
        self.base = base
        self.height = height


    def area(self):
        self.tri_area = self.base * self.height *0.5
        return self.tri_area

    def __str__(self) -> str:
        return  ('Area of Triangle '
                 + str(self.base) + 'Ux' + str(self.height)
                 + 'U :' + str(self.area()))

