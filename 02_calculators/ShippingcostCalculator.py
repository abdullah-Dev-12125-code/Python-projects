Base_Cost = 50
Weight_Rate = 10 
Distance_Rate = 5 



def calculate_shipping_cost(Weight,Distance):
    Cost= Base_Cost+(Weight*Weight_Rate)+(Distance*Distance_Rate)
    return Cost


def Apply_Discount(Cost):
    if Cost > 500:
        Percentage_Dis = Cost * 0.15
        Total = Cost - Percentage_Dis
        return Total
    elif 300 <= Cost <= 500:
        Percentage_Dis_LESS = Cost * 0.10 
        Totals = Cost - Percentage_Dis_LESS
        return Totals
    else:
        return Cost 
Name = input("Enter your name: ")
Address = input("Enter your address: ")
while True:
    try:
        Weight = int(input("Enter the weight of your package: "))
        Distance = int(input("Distance,The package will be shipped: "))
        break
    except ValueError:
        print("A numeric input is required!!")
    

Costs = calculate_shipping_cost(Weight,Distance)
Final_cost = Apply_Discount(Costs)


print("\n" + "-"*40)
print("\t\tShipping list")
print("-"*40)

print(f"Customer Name   : \t\t\t{Name}")
print(f"Address         :\t\t\t{Address}\n")

print("-"*40)

print(f"Package weight  :\t\t\t{Weight}Kg")
print(f"Net cost        :\t\t\t{Costs}$")
if Costs >=300:
    print(f"Total           :\t\t\t{Final_cost}$ (Discounted)")
else:
    print(f"Total           :\t\t\t{Final_cost}$ (No-Discount)")




