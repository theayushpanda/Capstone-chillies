# code chunk to calculate the total stock worth for a menu

menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# creating a dictionary to store the stock value

stock = {
    "Coffee": 20,
    "Tea": 30,
    "Sandwich": 15,
    "Cake": 10
}

# dictionary to store the price value

price = {
    "Coffee": 3.5,
    "Tea": 2.5,
    "Sandwich": 5.0,
    "Cake": 4.0
}

total_stock_worth = 0

# for loop to iterate each item on the dictionaries

for item in menu:
    
    # calculating total stock worth by adding every iteration to the variable total_stock_worth which is a result of the product of the parallel items in the dictionaries

    total_stock_worth += stock[item] * price[item]

print("The total stock worth in the cafe is: $", total_stock_worth)
