# Lab 13 - Inventory Control System

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]


def show_menu():
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")


def view_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")


def add_item():
    name = input("Enter item name to add: ").strip()
    if name == "":
        print("[ERROR] Item name cannot be empty.")
        return
    inventory.append(name)
    print(f'[SUCCESS] "{name}" added to inventory.')


def remove_item():
    name = input("Enter item name to remove: ").strip()
    if name in inventory:
        inventory.remove(name)
        print(f'[SUCCESS] "{name}" removed from inventory.')
    else:
        print(f'[ERROR] "{name}" not found in inventory.')


def sort_inventory():
    inventory.sort()
    print("\n[SUCCESS] Inventory sorted alphabetically.")
    print("Updated Inventory:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}")


print("=" * 50)
print("        INVENTORY CONTROL SYSTEM")
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        sort_inventory()
    elif choice == "5":
        print("\nThank you for using the Inventory Control System. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 5.")
