"""

Step 5:

Implements the print_menu() function to display a menu of options for manipulating the shopping cart.

* print_menu(ShoppingCart): Takes a ShoppingCart object as a parameter and prints a menu of options.
* Handles invalid input by prompting the user until a valid option is entered.
* Calls print_menu() in the main() function and continues to execute the menu until the user enters 'q' to quit.

Step 6:

Implements the "Output shopping cart" and "Output item's description" menu options.

* Output shopping cart: Calls print_total() on the ShoppingCart object to display the cart summary.
* Output item's description: Calls print_descriptions() on the ShoppingCart object to display item descriptions.
"""
from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    command = ""
    while command != 'q':
        print(menu)
        command = input("Choose an option: ")

        if command == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

        elif command == 'r':
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif command == 'c':
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the new item price: "))
            item_quantity = int(input("Enter the new item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.modify_item(item)

        elif command == 'i':
            cart.print_descriptions()

        elif command == 'o':
            cart.print_total()

        elif command == 'q':
            break

        else:
            print("Invalid option. Please choose again.")



def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    print_menu(cart)

if __name__ == '__main__':
    main()