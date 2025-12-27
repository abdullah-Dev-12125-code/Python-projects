while True:
    choice = int(input("1) Carat → Kg  2) Exit: "))
    if choice == 1:
        carat = float(input("Enter carat: "))
        grams = carat * 0.2
        kg = grams / 1000
        print(f"{carat} carat = {grams} g = {kg} kg")
    elif choice == 2:
        break
