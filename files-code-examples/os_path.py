"""
os.path
"""

import os
import sys

# get current working directory
path = os.getcwd()
print(path)

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# get file name
print(os.path.basename(path))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# get file path
print(os.path.dirname(path))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# split path
print(os.path.split(path))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# split directory by directory
print(path.split(os.path.sep))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# fetch file size
print(os.path.getsize(path))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# check if file exists
print(os.path.exists("/home"))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# is file?
print(os.path.isfile("."))

print("************")

choice = input("Your choice: ")
if choice == "n":
    sys.exit(1)

# is directory?
print(os.path.isdir("join.py"))
print(os.path.isdir("/Users"))
