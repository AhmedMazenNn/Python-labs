# Write a Python program to convert two lists into a
# dictionary in a way that item from list1 is the key
# and item from list2 is the value.


def dictconv(keys,values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result
while True:
    list1 = input("Please enter keys separated by space: ").split()
    if list1:
        break
    print("Keys cannot be empty. Please enter at least one key.")

while True:
    list2 = input("Please enter values separated by space: ").split()
    if list2:
        break
    print("Values cannot be empty. Please enter at least one value.")
new_list2 =[]

for value in list2:
    if value.isdigit():
        new_list2.append(int(value))
    else:
        new_list2.append(value)

if len(list1) != len(list2):
    print("Every key must have a value ")
else:
    dictionary = dictconv(list1, list2)
    print("Generated Dictionary:", dictionary)