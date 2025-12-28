prices = []

def total_price(prices, discount, tax):
    subtotal = sum(prices)
    discount_amount = subtotal * (discount / 100)
    tax_amount = subtotal * (tax / 100)
    final_total = subtotal - discount_amount + tax_amount
    return round(final_total, 2)

while True:
    items_Prices = input("Enter item price (or 'done'): ").strip().lower()

    if items_Prices == 'done':
        break

    if items_Prices.isdigit():
        print(f"{items_Prices} added to the list")
        prices.append(int(items_Prices))
    else:
        print("Invalid input! Please enter a number or 'done'.")

print(f"\nYour subtotal is: {sum(prices)}$")

while True:
    try:
        discount = int(input("Enter discount percentage (0 if none): "))
        break
    except ValueError:
        print("Enter a valid number!")

tax = 25

print("\nFinal total:", total_price(prices, discount, tax))
