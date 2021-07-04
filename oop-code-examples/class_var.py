"""
Class Variable
"""
import sys


class Student:

    university = "MIT"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


student_one = Student("John", "Tenth")

print(student_one.university)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

print(Student.university)
