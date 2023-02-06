building_shape=input("Enter the building's shape. (Round/Rectangle/Square): ")

if building_shape == "Round":
    radius = float(input("Enter the radius: "))
    area = 3.14*radius*radius
elif building_shape == "Rectangle":
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    area = length*breadth
elif building_shape == "Square":
    side = float(input("Enter the side: "))
    area = side*side

print("The area is: ", area)