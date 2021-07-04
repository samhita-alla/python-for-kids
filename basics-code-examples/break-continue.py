"""
break & continue
"""

# BREAK
num = 20
while True:
    print("*")
    num += 1
    if num == 23:
        break

print("*************")

# BREAK AND CONTINUE
while True:
    name = input("Who are you?")
    if name != "Joe":
        continue
    password = input("Hello, Joe. What is the password? (It is a fish.)")
    if password == "swordfish":
        break
print("Access granted.")
