# 3. Create package directory called Calculator and add
# file called my_functions that have the following
# function
# a. Sum Function
# b. Subtract Function
# c. Divide Function
# d. Multiply Function

def sum(a, b):
    print("Sum: ")
    return a + b

def subtract(a, b):
    print("sub: ")
    return a - b

def divide(a, b):
    print("divide: ")
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a / b

def multiply(a, b):
    print("multiply: ")
    return a * b
