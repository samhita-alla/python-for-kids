"""
List
"""
import sys

spam = ["cat", "bat", "rat", "elephant"]

# Indexing
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# Change values with indices
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# Concatenation
print([1, 2, 3] + ["A", "B", "C"])
print(["X", "Y", "Z"] * 3)
spam = [1, 2, 3]
spam = spam + ["A", "B", "C"]
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# Remove elements from list
spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# for loop with lists
supplies = ["pens", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# in and not in operators
print("howdy" in ["hello", "hi", "howdy", "heyas"])

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# multiple assignment
cat = ["fat", "black", "loud"]
size, color, disposition = cat
print(size)
print(color)
print(disposition)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# index
spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index("hello"))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# add values
spam = ["cat", "dog", "bat"]
spam.append("moose")
print(spam)
spam.insert(1, "chicken")
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# remove
spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat")
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# sort
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# sort by key
spam = ["a", "z", "A", "Z"]
spam.sort(key=str.lower)
print(spam)
