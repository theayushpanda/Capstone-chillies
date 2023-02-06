#code for storing names and returning the total number of names entered

name_list = []
while True:
    name = input("Enter a name: ")
    name_list.append(name)
    
    # stopping the loop when the user types 'stop'

    if name == "stop" or name == "STOP" or name == "Stop":
        name_list.pop()
        break

print("Total number of names you entered:", len(name_list))
   
