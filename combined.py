n = int("Enter a number:")

with open("numbers1.txt","w") as f:
    for i in range(0,n+1):
        f.write(i + ",")

with open("numbers2.txt","w") as g:
    for j in range(n,-1):
        g.write(j + ",")

with open("all_numbers.txt","w") as h:
    h.write()
