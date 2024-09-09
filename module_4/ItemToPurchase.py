'''
Program Outline: Shopping Cart Cost Calculator

This program calculates the total cost of a shopping cart containing two items.

Step 1: ItemToPurchase Class

- Attributes:
    * item_name (string): Name of the item
    * item_price (float): Price per unit of the item
    * item_quantity (int):  Number of units purchased

- Constructor:
    * Initializes attributes to default values:
        * item_name = "none"
        * item_price = 0
        * item_quantity = 0

- Method:
    * print_item_cost():  Prints the item name, quantity, price per unit, and total cost in the format:
        "Item Name Quantity @ $Price per Unit = $Total Cost"
'''

class ItemToPurchase():

    def __init__(self, item_name='none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} per Unit = ${total_cost:.2f}')