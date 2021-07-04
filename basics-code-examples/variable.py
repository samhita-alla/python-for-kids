"""
Variables
"""
import sys

# simple
spam = 40
print(spam)
eggs = 2
print(spam + eggs)
name = "Alice"
print(len(name))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# multiple assignemnt
a, b = "A", "B"
print(a)
print(b)
