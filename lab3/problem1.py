# Write a function in Python that accepts two string parameters. The ﬁrst parameter will be a string of characters,
# and the second parameter will be the same string of characters, but they’ll be in a different order and have one
# extra character. The function should return that extra character.
# ○
# For example, if the ﬁrst parameter is “eueiieo” and the second is “iieoedue,” then the function should
# return “d.”

def parameter(first: str, second: str):
    if not first.isalpha() or not second.isalpha():
        raise ValueError("Please enter valid strings containing only letters.")
    
    if len(second) != len(first) + 1:
        raise ValueError("The second string should have exactly one extra character.")

    for char in second:
        if second.count(char) > first.count(char):
            return char

first = input("Enter the first string: ").strip()
second = input("Enter the second string: ").strip()

try:
    extra_char = parameter(first, second)
    print(f"The extra character is: {extra_char}")
except ValueError as e:
    print(e)
