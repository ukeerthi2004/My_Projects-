def get_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Please enter a valid integer.")


def get_valid_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")
