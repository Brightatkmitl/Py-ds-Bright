import math

from shape import Shape


class Pentagon(Shape):
    def __init__(self, diagonal):
        self.Pentagon_area = 0.0


        self.diagonal = diagonal


    def area(self):
        self.Pentagon_area = (0.125 * self.diagonal * self.diagonal * (-5 + math.sqrt(45)) * math.sqrt(math.sqrt(20)+5))
        return self.Pentagon_area

    def __str__(self) -> str:
        return ('Area of Pentagon '
                + str(self.diagonal) + 'Ux = ' + str(self.area()))





