"""
Multiple Inheritance
"""


class RectangleArea:
    def rectangle_area(self, length, breadth):
        print(length * breadth)


class SquareArea:
    def square_area(self, length):
        print(f"Area is {length ** 2}")


class Area(RectangleArea, SquareArea):
    pass


obj = Area()
obj.rectangle_area(3, 4)
obj.square_area(9)
