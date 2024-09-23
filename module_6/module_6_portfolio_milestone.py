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
import re
from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

def get_current_date():
    date_pattern = re.compile(r'^(January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4}$')
    while True:
        date = input("Enter today's date (e.g., September 14, 2024): ")
        if date_pattern.match(date):
            return date
        else:
            print("Invalid date format. Please use the format 'Month (full name) DD, YYYY'.")


def check_value(prompt, value_type=float):
    """
    Prompts the user to enter a non-negative value.
    Args:
    prompt (str): The prompt message to display to the user.
    value_type (type): The type to which the user input should be cast. Default is float.

    Returns:
    float or int: A non-negative number entered by the user.
    """
    while True:
        try:
            user_val = value_type(input(prompt))
            if user_val < 0:
                print("Please enter a non-negative value.")
            else:
                return user_val
        except ValueError:
            print(f"Invalid input. Please enter a valid {value_type.__name__} larger than 0.")


def get_customer_name():
    pattern = re.compile(r'^[a-zA-Z\s]+$')
    while True:
        name = input("Enter customer's name (letters only): ")
        if pattern.match(name):
            return name
        else:
            print("Invalid name. Please use letters and spaces only.")


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
            item_price = check_value("Enter the item price: ", float)
            item_quantity = check_value("Enter the item quantity: ", int)
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
    customer_name = get_customer_name()
    current_date = get_current_date()
    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}", end='\n')

    print_menu(cart)

if __name__ == '__main__':
    main()