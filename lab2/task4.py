# Write a Program that takes a list of 5 numbers
# [3,6,4,0,8] then
# a. Remove the last element in list .
# b. Add in the second place ‘R’.
# c. Ask the user to input specific number in list
# then delete it { by taking the list element not
# index}.

list = ["3","6","4","0","8"]
print(list)

list.pop()
print("after deleteing last element",list)

list.insert(1,"R")
print("after inserting R in second positon", list)

delete = input("Enter the specific number in list to delete it: ")

if delete in list:
    list.remove(delete)
    print(f"After deleting '{delete}':", list)
else:
    print(f"'{delete}' is not in the list.")
