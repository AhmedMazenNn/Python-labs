# 4. Use the created Package in python code that takes
# input operand from User : 0->sum , 1->subtract ,
# 2->divide , 3 ->Multiple.
# a. If one of the two numbers is zero and operand
# is subtract raise Value Error with message “
# subtracting zero from Number “.
# b. If one of the two numbers is zero and operand
# is divide raise Zero division Error with message
# “ can’t divide with zero “.
# c. If one of the two numbers is zero and operand
# is Multiply raise Value Error with message “
# Multiply with Zero “.

# Import functions from the Calculator package
from task3_1 import sum, subtract, divide, multiply

def new_num():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect an operation:")
        print("0 -> Sum")
        print("1 -> Subtract")
        print("2 -> Divide")
        print("3 -> Multiply")

        operation = input("Enter your choice (0-3): ")

        if operation == "0":
            result = sum(num1, num2)
        elif operation == "1":
            if num1 == 0 or num2 == 0:
                raise ValueError("Subtracting zero from Number")
            result = subtract(num1, num2)
        elif operation == "2":
            if num2 == 0:
                raise ZeroDivisionError("Can not divide with zero")
            result = divide(num1, num2)
        elif operation == "3":
            if num1 == 0 or num2 == 0:
                raise ValueError("Multiply with Zero")
            result = multiply(num1, num2)
        else:
            print("Invalid choice! Please enter a number between 0-3.")
            return

        print(f"\nResult: {result}")

    except ValueError as ve:
        print(f"\nError: {ve}")
    except ZeroDivisionError as zde:
        print(f"\nError: {zde}")

new_num()
