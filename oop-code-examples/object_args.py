"""
Object Args
"""
import sys


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


# student_one = Student()
# Output?

student_one = Student("John", "Tenth")
print(student_one)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

print(student_one.name)
print(student_one.grade)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

student_one.name = "Oliver"
print(student_one)

