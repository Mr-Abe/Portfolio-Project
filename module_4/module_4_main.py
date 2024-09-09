"""
Program Outline: Shopping Cart Cost Calculator

This program calculates the total cost of a shopping cart containing two items.

Step 2: Main Program

- Prompt the user to enter details (name, price, quantity) for two items.
- Create two `ItemToPurchase` objects using the provided information.

Step 3: Calculate and Display Total Cost

- Calculate the total cost by summing the cost of each item (price * quantity).
- Print the total cost along with the individual item cost breakdowns.
"""
from ItemToPurchase import ItemToPurchase


def getNumItems():
    # Get the number of items from the user with validation
    while True:
        try:
            num_items = int(input('How many items would you like to add to the cart? '))
            if num_items <= 0:
                raise ValueError("The number of items must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")
        
    return num_items


def getItems():
    name = input('Please provide the name of your item: ')
    
    # Input validation for price
    while True:
        try:
            price = float(input('What was the price for the item? '))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative number.")

    # Input validation for quantity
    while True:
        try:
            quantity = int(input('How many items did you purchase? '))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative integer.")

    return ItemToPurchase(name, price, quantity)


def main():
    items = []
    num_items = getNumItems()

    for _ in range(num_items):
        item = getItems()
        items.append(item)
    
    print()

    for item in items:
        item.print_item_cost()

    total_cost = sum(item.total() for item in items)
    print(f'\nTotal Cost: ${total_cost:.2f}')


if __name__ == '__main__':
    main()
    