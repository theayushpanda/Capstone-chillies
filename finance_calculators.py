# investment calculator and a home loan calculator

import math

# asking the user to input their choice based among two options

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# investment case, asking the user for deposit value, interest rate, number of years and simpme/compound interest

if selection == "investment" or selection == "INVESTMENT" or selection == "Investment":
    deposit = float(input("How much do you want to deposit? "))
    interest_rate = float(input("What is you interest rate? (Enter without '%' sign) "))
    num_years = int(input("Enter the number of years you are investing? "))
    interest = input("Compound Interest or Simple Interest? (type 'simple' or 'compound)'")
    
    # calculating total return based on simple/compound interest
    if interest == 'simple':
        total_amount = deposit * (1 + (interest_rate / 100) * num_years)
    elif interest == 'compound':
        total_amount = deposit * math.pow((1 + (interest_rate / 100)), num_years)

    print("The amount you will get back is ", total_amount)

# bond case, asking the user for value, interest rate and term in months

elif selection == 'bond' or selection == 'BOND' or selection == 'Bond':
    value = float(input("Enter the value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the months you are planning to repay the bond in: "))
    
    # calculating bond repayment per month

    total_amount = (((interest_rate / 100) / 12) * value) / (1 - (1 + ((interest_rate / 100) / 12)) ** (-months))
    
    print("Your total monthly repayment is ", total_amount)

else:
    print("Your selection is invalid")