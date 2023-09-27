from shape import Shape


class Ellispe(Shape):
    def __init__(self, rad1 ,rad2 ):
        self.ellispe_area = 0.0
        self.rad1 = rad1
        self.rad2 = rad2
        self.pi = 3.14

    def area(self):
        self.ellispe_area = self.pi * self.rad1 * self.rad2
        return self.ellispe_area

    def __str__(self) -> str:
        return ('Area of ellispe '
                + str(self.rad1) + 'Ux' + str(self.rad2)
                + 'U :' + str(self.area()))
