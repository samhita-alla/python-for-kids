"""
Instance Method
"""

import sys


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def description(self):
        return f"Hey! I'm {self.name}"


student_one = Student("Meghan", "First")
print(student_one.description())

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Hey! I'm {self.name}"


student_one = Student("Meghan", "First")
print(student_one)
