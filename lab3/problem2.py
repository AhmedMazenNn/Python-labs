# Write a function that accepts a number as a parameter. The function should return a number that’s the difference
# between the largest and smallest numbers that the digits can form in the number.
# ○
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123
# subtracted from 321.

def number():
    input_num = input("Please enter a number: ")

    if not input_num.isdigit():
        print("Invalid input: Please enter a valid number.")
        return

    print("Valid input: It's a number!")

    small_num = int("".join(sorted(input_num)))
    big_num = int("".join(sorted(input_num, reverse=True)))

    result = big_num - small_num
    print(f"Smallest number: {small_num}")
    print(f"Largest number: {big_num}")
    print(f"Difference: {result}")

    return result 


number()
