main.py
def display_menu():
    print("\nMenu:")
    print("1. Pizza - $10")
    print("2. Burger - $8")
    print("3. Tacos - $6")
    print("4. Checkout")


def add_to_cart(choice, cart):
    if choice == "1":
        cart.append(("Pizza", 10))
    elif choice == "2":
        cart.append(("Burger", 8))
    elif choice == "3":
        cart.append(("Tacos", 6))


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item[1]
    return total


def main():
    cart = []
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "4":
            break
        elif choice in ["1", "2", "3"]:
            add_to_cart(choice, cart)
            print("Item added to cart.")
        else:
            print("Invalid option.")

    total = calculate_total(cart)
    print("\nReceipt:")
    for item in cart:
        print(f"{item[0]} - ${item[1]}")
    print(f"Total: ${total}")


main()
