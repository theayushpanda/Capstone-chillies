# code chunk for storing student ids in a .txt file 

num_students = int(input("Enter the number of students: "))

# writing reg_form.txt file + for loop for storing id for input number of students

with open("reg_form.txt","w") as f:

    for i in range(0,num_students):
    
        id = input("Enter your id: ")
    
    # writing along with a dotted line for signatures