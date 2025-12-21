def calculate_price(item1, item2, item3):
    if item1 <= 0 or item2 <= 0 or item3 <= 0:
        print("Please enter a valid value greater than 0.")
        return None
    return item1 + item2 + item3

while True:
    name = input("Enter your name: ")
    print(f"Welcome to the store, {name}")

    user_input = input("Enter the prices of items (separated by commas): ")
    item = user_input.split(',')

    try:
        item1 = float(item[0])
        item2 = float(item[1])
        item3 = float(item[2])
    except ValueError:
        print("Please enter numeric values only!")
        continue  

    total = calculate_price(item1, item2, item3)
    if total is not None:
        print(f"Your total is ({total})")
    discount = input("Do you have a membership(Yes/No): ").strip().lower()
    if discount == 'yes':
        code = input("Enter your membership discount code: ")
        if code == '3456':
            discount = 0.20
            discounting = total * discount
            finalprice = total - discounting
            print(f"{finalprice}")
            
        else:
            print("Enter a valid Membership discount code")
    if discount == 'no':
        print("Buy one to get 20% off")

        
       
        
    

           

       
