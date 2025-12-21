item_names = [
    ["Wireless Mouse", "19.99"],
    ["Keyboard", "49.50"],
    ["USB Cable", "5.75"],
    ["Laptop Stand", "29.99"],
    ["Headphones", "89.90"]
]

Shopping_cart = []

while True:
    item_input = input("Enter item name here (press '.' and enter when done): ").strip().lower()
    if item_input == '.':
        break

    found = False
    for item in item_names:
        if item_input == item[0].lower():  
            Shopping_cart.append(item)
            found = True
            break
    if not found:
        print("This item is not available!!")

print("\nYour Shopping Cart:")
for item in Shopping_cart:
    print(f"{item[0]} - ${item[1]}")

subtotal = sum(float(item[1]) for item in Shopping_cart)

discount_rate = 0.10
final_total = subtotal * (1 - discount_rate)

subtotal_str = "{:.2f}".format(subtotal)
final_total_str = "{:.2f}".format(final_total)

print(f"\nSubtotal: ${subtotal_str}")
print(f"Final Total after 10% discount: ${final_total_str}")
