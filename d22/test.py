import unittest
from main import process_orders

class TestProcessOrders(unittest.TestCase):
    def test_process_orders(self):
        self.assertRaises(
            ValueError,
            process_orders,
            [{"product": "apple", "quantity": 5}],
            {"banana": 3}
        )
        self.assertRaises(
            ValueError,
            process_orders,
            [{"product": "apple", "quantity": 5}],
            {"apple": 3}
        )
        self.assertEqual(
            process_orders([{"product": "apple", "quantity": 5}],{"apple": 5}),
            [{"product": "apple", "quantity": 5}]
        )

        inventory = {"apple": 10}
        process_orders([{"product": "apple", "quantity": 5}], inventory)
        self.assertEqual(
            inventory, {"apple": 5}
        )


if __name__ == '__main__':
    unittest.main()