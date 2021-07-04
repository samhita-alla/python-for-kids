"""
Default Parameter
"""
import math


class RectangleArea:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class SquareArea(RectangleArea):
    def __init__(self, length=3):
        super().__init__(length, length)

    # Extend
    def perimeter(self):
        return f"Perimeter of square is: {4 * math.sqrt(self.area())}"


square = SquareArea()
print(square.perimeter())
