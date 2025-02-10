# Create 2 dictionaries and append the two in one
# .{take into consideration unique keys }

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

new_dict = dict1.copy() 
new_dict.update(dict2)

print("Merged Dictionary:", new_dict)
