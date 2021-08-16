"""
Encapsulation
"""
import sys

# Public Attributes
class RectangleArea:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


rectangle = RectangleArea(10, 9)
print(rectangle.length)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# Protected Attribute
class RectangleArea:
    def __init__(self, length, breadth):
        self._length = length
        self.breadth = breadth


rectangle = RectangleArea(10, 9)
print(rectangle._length)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# Private Attribute
class RectangleArea:
    def __init__(self, length, breadth):
        self.__length = length
        self.breadth = breadth


rectangle = RectangleArea(10, 9)

# Every member with a double underscore will be changed to _object._class__variable
print(rectangle._RectangleArea__length)
