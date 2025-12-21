inventory = {}

while True:
    item = input("\nEnter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[item] = quantity

    choice = input("Do you want to add another item? (yes/no): ").lower()
    if choice == "no":
        break

print("\n Store Inventory List:")

for item, qty in inventory.items():
    print(f"Item: {item:<15} | Quantity: {qty}")

print("Total items :", len(inventory))

