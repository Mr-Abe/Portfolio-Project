import unittest
from unittest.mock import patch
from io import StringIO
from ItemToPurchase import ItemToPurchase
import module_4_main  

class TestShoppingCart(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', 'Bread', '2.50', '2', 'Milk', '1.99', '3', 'Eggs', '3.00', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_shopping_cart(self, mock_stdout, mock_input):
        module_4_main.main()  # Replace with the actual name of your main function in the program

        # Expected output
        expected_output = (
            "Bread 2 @ $2.50 per Unit = $5.00\n"
            "Milk 3 @ $1.99 per Unit = $5.97\n"
            "Eggs 1 @ $3.00 per Unit = $3.00\n"
            "\nTotal Cost: $13.97\n"
        )

        # Assert that the output is as expected
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
