import unittest

from controllers.order_controller import OrderController


class Test_OrderController(unittest.TestCase):
    def test_orders_(self):
        orders = [40, 60, 15]
        n_max = 100
        expected_orders = 4

        how_many = OrderController().combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders)

    def test_orders(self):
        orders = [50, 70, 40, 30, 20]
        n_max = 100
        expected_orders = 3

        how_many = OrderController().combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders)

    def test_orders_odd(self):
        orders = [80, 30, 60, 70, 40, 50]
        n_max = 100
        expected_orders = 2

        how_many = OrderController().combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders)


if __name__ == '__main__':
    unittest.main()
