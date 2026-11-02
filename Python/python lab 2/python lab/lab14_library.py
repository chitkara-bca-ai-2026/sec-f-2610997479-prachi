# Lab 14 - Library Book Collection (tuples and sets)

# Each book is an immutable tuple: (title, author, year, category)
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]

# Unique genres in the library
library_categories = set()
for book in books:
    library_categories.add(book[3])

# Genres requested by students
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}


def show_menu():
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")


def view_books():
    print("\n--- Current Library Catalog (Fixed Records) ---")
    for i, book in enumerate(books, start=1):
        title, author, year, category = book  # tuple unpacking
        print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')
    print(f"Total Books: {len(books)}")


def add_book():
    print("\n--- Add New Book Record ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    category = input("Enter category/genre: ").strip()

    if not (title and author and year and category):
        print("\n[ERROR] All fields are required. Book not added.")
        return

    new_book = (title, author, year, category)  # immutable tuple
    books.append(new_book)
    library_categories.add(category)
    print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
    print(f'[INFO] Category set updated with: "{category}"')


def view_categories():
    print("\n--- Unique Categories Available in Library (Set) ---")
    for category in sorted(library_categories):
        print(f"  - {category}")
    print(f"Total Unique Genres: {len(library_categories)}")


def add_to_wishlist():
    print("\n--- Add to Student Wishlist ---")
    category = input("Enter requested category: ").strip()
    if category == "":
        print("[ERROR] Category cannot be empty.")
        return
    student_wishlist.add(category)
    print(f'[SUCCESS] "{category}" added to student wishlist.')


def gap_analysis():
    print("\n" + "=" * 15 + " CATEGORY GAP ANALYSIS " + "=" * 15)
    print("Library Holdings (Set): ", sorted(library_categories))
    print("Student Wishlist (Set): ", sorted(student_wishlist))
    print("-" * 52)

    in_stock = library_categories & student_wishlist
    to_purchase = student_wishlist - library_categories
    combined = library_categories | student_wishlist

    print("\n1. Already in Stock (Intersection &):")
    print("  ", sorted(in_stock))
    print("\n2. Purchase Order Needed (Difference -):")
    print("  ", sorted(to_purchase))
    print("\n3. Full Combined Genre Coverage (Union |):")
    print("  ", sorted(combined))
    print("=" * 52)


print("=" * 50)
print("        LIBRARY BOOK & CATEGORY MANAGER")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        view_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        view_categories()
    elif choice == "4":
        add_to_wishlist()
    elif choice == "5":
        gap_analysis()
    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 6.")
