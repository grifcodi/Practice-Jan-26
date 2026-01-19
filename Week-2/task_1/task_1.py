def square_area(a):
    return a**2

def rectangle_area(a, b):
    return a * b

def triangle_area(b, h):
    return b * h * 0.5

def circle_area(r):
    pi = 3.14
    return pi * r ** 2

print("Square:", square_area(4))
print("Rectangle:", rectangle_area(3, 5))
print("Triangle:", triangle_area(6, 4))
print("Circle:", circle_area(2))
print('\n')

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius ** 2

shapes = [
    Square(4),
    Rectangle(3, 5),
    Triangle(6, 4),
    Circle(2)
]

for shape in shapes:
    print(type(shape).__name__, "area = ", shape.area())