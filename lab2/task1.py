# Write a Python function to check whether a number
# falls in a given range. Range (-5, 5) -> return TRUE

while(True):
    input_num = input("Enter a number: ")
    if input_num.isnumeric():
        input_num = int(input_num)
        break
    else:
        print("Please enter a number")
    
def check(num):
    if num in range(-5,6):
        return True
    else:
        return False

print(check(input_num))