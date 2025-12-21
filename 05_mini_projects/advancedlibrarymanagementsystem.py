book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

book_category = []
shelf_number = []
book_number = []
publisher_code = []


def category_of_book():
    for code in book_codes:
        book_category.append(code[:3])

def shelf_number_of_books():
    for shelf in book_codes:
        shelf_number.append(shelf[3:5])

def Unique_number_of_book():
    for book in book_codes:
        book_number.append(book[5:8])

def publishers_code():
    for publish in book_codes:
        publisher_code.append(publish[8:])


category_of_book()
shelf_number_of_books()
Unique_number_of_book()
publishers_code()


print("Category of book is |",book_category)
print("\nShelf number of book is |",shelf_number)
print("\nUnique code of book is |",book_number)
print("\nPublishers code is |",publisher_code)

print("\n| Organized Books |\n")

for search in book_category:
    if search == 'FIC':
        print("This book is in fiction category",search)
    elif search == 'BIO':
        print("This  book is related to biology",search)
    elif search == 'SCI':
        print("The book is related to science",search)
    else:
        print("No books found!")

                
