# code chunk to print numbers 1 to 1000 by writing only two lines of code

num = list(range(1,1001))
print(num)

# printing only even numbers from 1 ro 1000

for i in num:
    if i%2 == 0:
        print(i)
        i += 1
    
        