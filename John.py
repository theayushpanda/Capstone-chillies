# code chunk for taking name input using a while loop, which breaks when "john" is entered and returns all names except John

names_list = []
name = input("Enter a name: ")

# while loop to add names that are not john

while name.lower() != "john":
    names_list.append(name)
    name = input("Enter a name: ")

#break statement

    if name == "john":
        break

print(names_list)
