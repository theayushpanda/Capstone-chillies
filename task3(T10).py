# creating a while loop that countdowns from 20 to 0

count = 20
while count >=0:
    print(count)
    count -= 1

# creating a while that returns all even numbers between 1 and 20
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# creating a for loop to print a star pyramid

for i in range(1,6):
    print("*" * i)


# calculating Greatest common divisor of two positive integers
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# condition to check for positive integers

if num1 > 0 and num2 > 0:
    print("The greatest Common Divisor or Highest Common Factor is :", math.gcd(num1,num2))
else:
    print("Wrong input")

