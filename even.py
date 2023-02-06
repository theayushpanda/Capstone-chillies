def even_numbers(n):
    even_list = []
    i = 2
    while i <= n:
        if i % 2 == 0:
            even_list.append(i)
        i += 1
    return even_list

n=int(input("Enter a number: "))

print(even_numbers(n))
