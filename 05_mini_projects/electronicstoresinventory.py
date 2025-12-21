inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

inventory.update({
    "Smartphone": inventory["Smartphone"] + 10,
    "Headphones": inventory["Headphones"] + 5
})

print("Updated inventory after new shipment:")
for item, qty in inventory.items():
    print(f"{item}: {qty}")

last_item, last_qty = inventory.popitem()
print(f"\nSold item: {last_item} | Quantity: {last_qty}")

camera_stock = inventory.get("Camera", "Out of Stock")
print(f"\nCamera stock status: {camera_stock}")
