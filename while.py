# code for returning average of input numbers

num_list = []
total = 0

# while loop for input of numbers

while True:
    num = int(input("Enter a number: "))
    num_list.append(num)
    total += num

# stopping the loop when user inputs -1

    if num == -1:
        num_list.pop()
        break

# calculating and printing the average

average = total / len(num_list)
print("The average is:", average)