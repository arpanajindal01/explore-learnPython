class Shape:
    def __init__(self, name : str):
        self.name = name

class Square(Shape):
    def __init__(self, side: int):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius **2)


class Triangle(Shape):
    def __init__(self, base: int, height: int):
        super().__init__("Rectangle")
        self.base = base
        self.height = height

    def area(self):
        return self.base * 0.5 * self.height


my_square = Square(10)
print(f"Side of the {my_square.name} is {my_square.side} having area of {my_square.area()}")

my_circle = Circle(20)
print(f"Radius of {my_circle.name} is {my_circle.radius} having area of {my_circle.area()}")

my_rectangle = Rectangle(10, 20)
print(f"Length of {my_rectangle.name} is {my_rectangle.length} and width is {my_rectangle.width} having area of {my_rectangle.area()}")

my_triangle = Triangle(10, 15)
print(f"Base of {my_triangle.name} is {my_triangle.base} and height is {my_triangle.height} having area of {my_triangle.area() }")


