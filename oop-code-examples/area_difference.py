"""
Assignment Question

Write a function, area_difference, that takes two Rectangle instances (note: "Rectangle" is a class) as parameters and returns the signed difference in area between them. 
"signed difference" means that rather than always returning a positive number, the sign of the return value should be negative 
if the first rectangle is smaller. Test your code with: 

    rectange_one = Rectangle(3, 4)
    rectange_two = Rectangle(4, 4)
    print(area_difference(rectange_one, rectange_twp))
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def area_difference(r1, r2):
    return (r1.width * r1.height) - (r2.width * r2.height)


# TEST
rectange_one = Rectangle(3, 4)
rectange_two = Rectangle(4, 4)
print(area_difference(rectange_one, rectange_two))
