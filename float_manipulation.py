# code chunk for taking 10 float input and printing the sum, average, maximum, minimum, median

import math

#declaring the list

num_list = []

# for loop for adding inputs to the list

for i in range(0,10):
    num = float(input("Enter a number: "))
    num_list.append(num)

# calculations

sum = sum(num_list)

maximum = max(num_list)

minimum = min(num_list)

index_max = num_list.index(maximum)

index_min = num_list.index(minimum)

average = sum / len(num_list)

median = len(num_list)/2


print(sum)
print(index_max)
print(index_min)
print(round(average))
print(median)
