import math

side1=float(input("Enter side length:"))
side2=float(input("Enter 2nd side length:"))
side3=float(input("Enter 3rd side length:"))

s=(side1+side2+side3)/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print("Area of the triangle is:", area)