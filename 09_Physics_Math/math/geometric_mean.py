import math

numbers = []

while True:
    num = input("Enter number (or 'done' to finish): ")
    if num.lower() == "done":
        break
    
    numbers.append(float(num))
    gm = math.prod(numbers) ** (1 / len(numbers))  
    Product = math.prod(numbers)
print("Prod =", Product, "GM =", gm)