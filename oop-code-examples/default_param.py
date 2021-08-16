"""
Default Parameter
"""


class RectangleArea:
    def __init__(self, length=5, breadth=3):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# no length given, will this work?
rectangle = RectangleArea()
print(rectangle.area())
