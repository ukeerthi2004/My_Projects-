DATA_FILE = "inventory_data.txt"

def read_inventory():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            inventory = []
            for line in lines:
                parts = line.strip().split(",")
                inventory.append({
                    "id": parts[0],
                    "name": parts[1],
                    "quantity": int(parts[2]),
                    "price": float(parts[3])
                })
            return inventory
    except FileNotFoundError:
        return []


def write_inventory(inventory):
    with open(DATA_FILE, "w") as file:
        for item in inventory:
            file.write(f"{item['id']},{item['name']},{item['quantity']},{item['price']}\n")
