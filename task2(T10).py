# creating a program to print leap and non leap years in a given time frame

# creating a function for testing leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

start_year = int(input("What year do you want to start with: "))            #asking for input
num_years = int(input("How many year do you want to check? "))

# for loop to print
current_year = start_year
for i in range(num_years):
    if is_leap_year(current_year):
        print(f"{current_year} is a leap year.")
    else:
        print(f"{current_year} is not a leap year.")
    current_year += 1