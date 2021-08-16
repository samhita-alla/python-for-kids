"""
Extend
"""
import math


class RectangleArea:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class SquareArea(RectangleArea):
    def __init__(self, length):
        super().__init__(length, length)

    # Extend
    def perimeter(self):
        return f"Perimeter of square is: {4 * math.sqrt(self.area())}"


square = SquareArea(3)
print(square.area())
print(square.perimeter())
