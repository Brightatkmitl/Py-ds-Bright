# area_calc.py
from Bright.rectangle import Rect
from Bright.square import Square
from Circle import Circle
from Triangle import Triangle
from Ellispe import Ellispe
from Pentagon import Pentagon

if __name__ == '__main__':
    sq1 = Square(5)
    print(sq1)
    print(sq1.area())

    rect1 = Rect(5, 10)
    rect2 = Rect(7, 9)
    print(rect1)
    print(rect2)

    print(" Homework outputs below ")

    print(Circle(5))
    print(Triangle(2,1))
    print(Ellispe(5,5))
    print(Pentagon(5))

