num=int(input("Enter an Integer: "))
if num%2 == 0 and num%5 == 0:
    print("The number is divisible by 2 and 5")
elif num%2 == 0:
    print("The number is divisible by 2")
elif num%5 == 0:
    print("The number is divisible by 5")
elif num%2 !=0 or num%5 !=0:
    print("The number is not divisible by 2 or 5")