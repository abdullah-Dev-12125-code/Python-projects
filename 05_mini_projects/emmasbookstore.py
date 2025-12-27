books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 11.50
}

backup_dicct =books.copy()

print("\n Current inventory list!!\n")
print(f"{books}\n")

print("The Total price of books\n")

total = 0
for name, price in books.items():
    print("Book:", name, "| Price:", price)
    total += price

print("\nTotal price of all books:\n", f"{total}\n")

bought = input("Enter name of books that has been sold!!: ")

if bought in books:
    books[bought] = "sold"
    print(f"{bought} has been sold!\n")
else:
    print("This book is not in the inventory!!")

for name,price in books.items():
    print(f"The Book:{name} | price:{price}")





