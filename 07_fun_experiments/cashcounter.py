itemswant = input("Enter the item you want: ")

items = {
    "apple": 20,
    "apple cider": 40,
    "orange juice": 60,
    "milk": 50,
    "coco powder": 160,
    "lobster": 400,
    "fish": 600,
    "Fried chicken": 350
}

if itemswant in items:
    # Get the price of the selected item
    price = items[itemswant]
    print(f"{itemswant} costs {price}")
else:
    print("Sorry, this item is not available.")
