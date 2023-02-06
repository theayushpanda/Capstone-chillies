num1 = 3
num2 = 4
num3 = 5
if num2 > num1:
    print(num2)
else:
    print(num1)

if num1%2 == 0:
    print("num1 is even")
else:
    print("num1 is odd")

if num1 >= num2 and num1 >= num3:
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 >= num1 and num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)   