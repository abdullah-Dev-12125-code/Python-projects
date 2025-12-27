Bookshelf = ["Harry Potter series", "Lord Of The Rings", "The Great Gatsby"]

while True:

    print("\n1. Check the whole list")   
    print("2. Add a book in the library")  
    print("3. Remove a book from the library") 
    print("4. Check if a book is in the library")   
    print("5. Exit")

    choice = int(input("\nChoose (1,2,3,4,5): "))    

    if choice == 1: 
        print(f"\nBookshelf: {Bookshelf}")    

    elif choice == 2:   
        while True:
            AddBook = input("Enter the book name (or type 'done' when done): ").strip()
            if AddBook.lower() == 'done':
                print(f"Updated bookshelf: {Bookshelf}")
                break
            elif AddBook in Bookshelf:
                print("This book is already in the Bookshelf.")
            else:
                Bookshelf.append(AddBook) 
                print(f"The book '{AddBook}' is added to the bookshelf.")
                

    elif choice == 3:
        remove = input("Enter the name of the book you want to remove: ").strip()
        if remove in Bookshelf:
            Bookshelf.remove(remove)
            print(f"The book '{remove}' was removed.")
            print(f"Updated bookshelf: {Bookshelf}")
        else:
            print("The book is not in the list.")

    elif choice == 4:
        Locatebook = input("Enter the book name to check: ").strip()
        if Locatebook in Bookshelf:
            print("The book is available!")
        else:
            print("Sorry! It is not available.")

    elif choice == 5:
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")





