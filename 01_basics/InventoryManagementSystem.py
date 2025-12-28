inventory = ()

while len(inventory) < 5:
    fruit = input("Enter name of fruits: ")
    inventory += (fruit,)
print("Here is the current list",inventory)

Newinventory = list(inventory)

Remove = input("Enter item you want to remove: ")
if Remove in Newinventory:
    Newinventory.remove(Remove)
    print(Newinventory)

add = input("Enter fruits name you want to add: ")
Newinventory.append(add)

oldinventory = tuple(Newinventory)

print("\n final list\n")
print(oldinventory)
