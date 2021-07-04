"""
Dictionary
"""

import sys

# simple
myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(myCat["size"])

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# equal?
eggs = {"name": "Zophie", "species": "cat", "age": "8"}
ham = {"species": "cat", "age": "8", "name": "Zophie"}
print(eggs == ham)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# keys, vals, items
spam = {"color": "red", "age": 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# in
spam = {"name": "Zophie", "age": 7}
print("color" in spam.keys())

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# get
picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get("cups", 0)) + " cups.")
