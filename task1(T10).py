# code to print n table upto 12

n = int(input("Enter a number: "))
for x in range(n, n + 1):
    
    for y in range(1,13):
        
# writing printing formula 

        print(f"{x} * {y} = {x*y}")
    
    print("")
    