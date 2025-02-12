# 1. Write a Python program to read a file line by line
# and store it into a list.
# Open the file in read mode
with open("task1.txt", "r") as t1:
    lines = t1.readlines()
print(lines)
