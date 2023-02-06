cycling_time=int(input("Enter cycling time: "))
swimming_time=int(input("Enter swimming time: "))
running_time=int(input("Enter running time: "))

total_time = cycling_time + swimming_time + running_time

print("Total time to complete the marathon is: ", total_time)

if total_time < 100:
    print("You are awarded with Provincial Colours")
elif total_time > 100 and total_time < 105:
    print("You are awarded with Provincial Half Colours")
elif total_time > 105 and total_time < 110:
    print("You are awarded with Provincial Scroll")
else:
    print("No Award")