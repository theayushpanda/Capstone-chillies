from ast import If


item_price=float(input("Enter the item price: "))
distance=float(input("Enter the delivery distance in kms: "))
transport=input("Transport (Air/Freight? ")
insurance=input("Insurance (Full/Limited) ")
gift=input("Is it a gift? (y/n) ")
delivery=input("Delivery (Priority/Standard)? ")

if transport=="Air":
    cost_transport_air=0.36*distance
else:
    cost_transport_air=0.25*distance
if insurance=="Full":
    insurance_cost=50
else:
    insurance_cost=25
if gift=="y":
    gift_cost=15
else:
    gift_cost=0
if delivery=="Priority":
    delivery_cost=100
else:
    delivery_cost=20

total_cost = item_price + cost_transport_air + insurance_cost + gift_cost + delivery_cost

print("The total cost of your order is: ", total_cost)
            
