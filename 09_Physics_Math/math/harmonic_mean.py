numbers = []
reciprocals = []

while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == "done":
        break
    
    n = float(num)
    numbers.append(n)
    reciprocals.append(1 / n)  


print("Reciprocals of each number:")
for i, r in enumerate(reciprocals, 1):
    print(f"1/{numbers[i-1]} = {r}")

hm = len(numbers) / sum(reciprocals)
print("\nHarmonic Mean =", hm)
