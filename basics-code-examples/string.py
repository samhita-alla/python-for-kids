"""
Primitive Data Types
"""
import sys

print("Bob" * 13)
# print("Bob" * 10.0)
print("Alice" + "Bob")
# print("Alice" + 13)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# isX method
print('hello'.isalpha())
print('123'.isdecimal())
print('This Is Title Case 123'.istitle())
