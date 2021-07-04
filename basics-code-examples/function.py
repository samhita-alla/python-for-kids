"""
Functions
"""
import sys

# simple
def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


hello()
hello()
hello()

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# parameters
def hello(name):
    return "Hello " + name


print(hello("Alice"))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# slides
# local & global scope
def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)


# local and global with same name
def spam():
    eggs = "spam local"
    print(eggs)


def bacon():
    eggs = "bacon local"
    print(eggs)
    spam()
    print(eggs)


eggs = "global"
bacon()
print(eggs)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# global keyword
def spam():
    global eggs
    eggs = "spam"


eggs = "global"
spam()
print(eggs)
