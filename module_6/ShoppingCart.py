"""
ShoppingCart Class Specification:

Step 4:

This class represents a shopping cart for a customer, storing items and providing methods to manage and display cart contents.

Data Attributes:

* customer_name (string): The name of the customer associated with the cart. Defaults to "none".
* current_date (string): The current date. Defaults to "January 1, 2020".
* cart_items (list): A list to store ItemToPurchase objects representing items in the cart.

Methods:

* __init__(customer_name="none", current_date="January 1, 2020"): Initializes a ShoppingCart object with optional customer name and date.
* add_item(ItemToPurchase): Adds an ItemToPurchase object to the cart_items list.
* remove_item(item_name): Removes an item from the cart_items list by its name. Prints an error message if the item is not found.
* modify_item(ItemToPurchase): Modifies an existing item's description, price, or quantity if found in the cart. Prints an error message if not found.
* get_num_items_in_cart(): Returns the total quantity of all items in the cart.
* get_cost_of_cart(): Calculates and returns the total cost of all items in the cart.
* print_total(): Prints a formatted summary of the cart, including the customer name, date, number of items, itemized costs, and total cost. If the cart is empty, prints "SHOPPING CART IS EMPTY".
* print_descriptions(): Prints a formatted list of item descriptions in the cart, including the customer name and date."""
from ItemToPurchase import ItemToPurchase
class ShoppingCart():
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_2_find):
        found = False
        for item in self.cart_items:
            if item.item_name == item_2_find:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print(f"Nothing removed, {item_2_find} not found.")
    

    def modify_item(self, item):
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                # Modify the item's attributes
                self.cart_items[i].item_price = item.item_price
                self.cart_items[i].item_quantity = item.item_quantity
                return
        print(f"{item} not found in cart.")


    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.total() for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()