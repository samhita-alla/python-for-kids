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


rectange = RectangleArea(10, 9)
print(rectange.area())

square = SquareArea(3)
print(square.area())
