from storage import read_inventory, write_inventory
from utils import get_valid_int, get_valid_float


# ✅ Auto Generate Product ID
def generate_product_id(inventory):
    if not inventory:
        return "1001"
    else:
        last_id = max(int(item["id"]) for item in inventory)
        return str(last_id + 1)


# ✅ Add Product (Auto ID)
def add_product():
    inventory = read_inventory()

    pid = generate_product_id(inventory)
    print(f"🆔 Auto Generated Product ID: {pid}")

    name = input("Enter Product Name: ")
    quantity = get_valid_int("Enter Quantity: ")
    price = get_valid_float("Enter Price: ")

    inventory.append({
        "id": pid,
        "name": name,
        "quantity": quantity,
        "price": price
    })

    write_inventory(inventory)
    print("✅ Product added successfully!")


# ✅ Beautiful Table Display
def view_products():
    inventory = read_inventory()

    if not inventory:
        print("No products found.")
        return

    print("\n" + "="*60)
    print(f"{'ID':<10}{'Name':<20}{'Qty':<10}{'Price (₹)':<10}")
    print("="*60)

    for item in inventory:
        print(f"{item['id']:<10}{item['name']:<20}{item['quantity']:<10}{item['price']:<10}")

    print("="*60)


# ✅ Search Product
def search_product():
    pid = input("Enter Product ID to search: ")
    inventory = read_inventory()

    for item in inventory:
        if item["id"] == pid:
            print("\n✅ Product Found:")
            print(item)
            return

    print("❌ Product not found.")


# ✅ Update Product
def update_product():
    pid = input("Enter Product ID to update: ")
    inventory = read_inventory()

    for item in inventory:
        if item["id"] == pid:
            item["name"] = input("Enter new name: ")
            item["quantity"] = get_valid_int("Enter new quantity: ")
            item["price"] = get_valid_float("Enter new price: ")

            write_inventory(inventory)
            print("✅ Product updated!")
            return

    print("❌ Product not found.")


# ✅ Delete Product
def delete_product():
    pid = input("Enter Product ID to delete: ")
    inventory = read_inventory()

    new_inventory = [item for item in inventory if item["id"] != pid]

    if len(new_inventory) == len(inventory):
        print("❌ Product not found.")
    else:
        write_inventory(new_inventory)
        print("✅ Product deleted!")


# ✅ Export to Excel (CSV)
def export_to_excel():
    inventory = read_inventory()

    if not inventory:
        print("No data to export.")
        return

    with open("inventory_export.csv", "w") as file:
        file.write("ID,Name,Quantity,Price\n")
        for item in inventory:
            file.write(f"{item['id']},{item['name']},{item['quantity']},{item['price']}\n")

    print("✅ Inventory exported to inventory_export.csv (Open in Excel)")


# ✅ Main Menu
def menu():
    while True:
        print("\n==== Inventory Management System ====")
        print("1. Add Product (Auto ID)")
        print("2. View Products (Table)")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Export to Excel")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            export_to_excel()
        elif choice == "7":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
