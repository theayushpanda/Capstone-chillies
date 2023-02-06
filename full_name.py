name=input("Enter your full name: ")

if len(name)==0:
    print("You haven't entered anything. Please enter your full name.")
elif len(name)<4:
    print("You have entered less than 4 characters. Please make sure that you have entered your full name.")
elif len(name)>25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")