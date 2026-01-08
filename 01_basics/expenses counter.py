expenses = []

def Add_expenses():
    try:
        category = input("Enter category: ").capitalize()
        amount = float(input("Enter amount: "))
        short_note = input("Enter description: ")
        expense = {
            "category": category,
            "amount": amount,
            "short_note": short_note
        }
        expenses.append(expense)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except Exception as e:
        print("Unexpected error:", e)


def view_expenses():    
    try:
        if not expenses:
            print("No records found!")
            return
        
        total = 0
        print("\n--- Expense List ---")
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['category']} - Rs.{exp['amount']:.2f} ({exp['short_note']})")
            total += exp['amount']
        
        print("\nTotal Expense: Rs.", total)
    except Exception as e:
        print("Something went wrong!", e)


def search_by_category():
    try:
        if not expenses:
            print("No records found")
            return
        cat = input("Enter category to search: ").capitalize()
        found = [e for e in expenses if e["category"] == cat]
        if not found: 
            print("No expenses found for this category")
            return
        print(f"\n--- Expenses in {cat} ---")
        for e in found:
            print(f"Rs-{e['amount']:.2f} ({e['short_note']})")
    except Exception as e:
        print("Something went wrong!!!", e)


def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            Add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


menu()
