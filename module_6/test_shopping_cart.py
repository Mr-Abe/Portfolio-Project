import unittest
from unittest.mock import patch
from io import StringIO
from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart
from module_6_portfolio_milestone import print_menu  # Assuming your main module is ShoppingCart.py

class TestShoppingCart(unittest.TestCase):
    maxDiff = None

    @patch('builtins.input', side_effect=[
        'John Doe', 'March 20, 2023',  # Customer name and date
        'a', 'Bread', 'Bread description', '2.50', '2',  # Add item 1
        'a', 'Milk', 'Milk description', '1.99', '3',  # Add item 2
        'o',  # Output shopping cart
        'q'   # Quit
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_items_and_print_cart(self, mock_stdout, mock_input):
        cart = ShoppingCart(customer_name="John Doe", current_date="March 20, 2023")
        print_menu(cart)

        # Print the actual output for debugging
        actual_output = mock_stdout.getvalue()
        print("Actual Output:\n", actual_output)

        # Expected output for the test case
        expected_output = (
            "\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
            "Choose an option: "
            "Enter the item name: "
            "Enter the item description: "
            "Enter the item price: "
            "Enter the item quantity: "
            "Choose an option: "
            "Enter the item name: "
            "Enter the item description: "
            "Enter the item price: "
            "Enter the item quantity: "
            "Choose an option: "
            "John Doe's Shopping Cart - March 20, 2023\n"
            "Number of Items: 5\n"
            "Bread 2 @ $2.50 per Unit = $5.00\n"
            "Milk 3 @ $1.99 per Unit = $5.97\n"
            "\nTotal: $10.97\n"
            "Choose an option: "
        )

        # Print the expected output for debugging
        print("Expected Output:\n", expected_output)

        # Assert that the output is as expected
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()