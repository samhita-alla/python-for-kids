"""
Objects are mutable!
"""
import sys


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} belongs to {self.grade} grade."


student_one = Student("John", "Tenth")
print(student_one)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

student_one.name = "Samhita"
print(student_one)
