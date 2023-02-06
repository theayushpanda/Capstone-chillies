product1=input("Enter a product name: ")
product2=input("Enter second product name: ")
product3=input("Enter third product name: ")

price1=float(input("Enter precise price (upto 2 decimals) for product1: "))
price2=float(input("Enter precise price (upto 2 decimals) for product2: "))
price3=float(input("Enter precise price (upto 2 decimals) for product3: "))

sum_price=price1+price2+price3
avg_price=round(sum_price/3)

print("The Total of", product1, product2, product3, "is",sum_price,"and the average price of the items is ",avg_price)
