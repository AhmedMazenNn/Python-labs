# 2. Create a list of strings , Add to it yourname then
# Write the list to a new File .

lines = ["JS", "Python", "Java"]
name = "mazen"

lines.append(name)


with open("task2.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
    print(lines)

