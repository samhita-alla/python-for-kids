"""
Override
"""


class RectangleArea:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class SquareArea(RectangleArea):
    def __init__(self, length):
        super().__init__(length, length)

    # Override
    def area(self):
        return f"Area is {self.length * self.breadth}"


rectangle = RectangleArea(10, 9)
print(rectangle.area())

square = SquareArea(3)
print(square.area())
