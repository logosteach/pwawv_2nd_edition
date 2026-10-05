import unittest
from shipping import shipping_cost


class TestShippingNormal(unittest.TestCase):

    def test_light_package(self):
        self.assertEqual(shipping_cost(0.5), 5.00)

    def test_medium_package(self):
        self.assertEqual(shipping_cost(3), 8.50)

    def test_heavy_package(self):
        self.assertEqual(shipping_cost(10), 12.00)


class TestShippingEdges(unittest.TestCase):

    def test_exactly_1_kg(self):
        self.assertEqual(shipping_cost(1), 5.00)

    def test_just_over_1_kg(self):
        self.assertEqual(shipping_cost(1.01), 8.50)

    def test_exactly_5_kg(self):
        self.assertEqual(shipping_cost(5), 8.50)

    def test_just_over_5_kg(self):
        self.assertEqual(shipping_cost(5.01), 12.00)

    def test_tiny_package(self):
        self.assertEqual(shipping_cost(0.01), 5.00)


class TestShippingInvalid(unittest.TestCase):

    def test_zero_weight_raises(self):
        with self.assertRaises(ValueError):
            shipping_cost(0)

    def test_negative_weight_raises(self):
        with self.assertRaises(ValueError):
            shipping_cost(-2)

    def test_text_weight_raises(self):
        with self.assertRaises(TypeError):
            shipping_cost("3")


if __name__ == "__main__":
    unittest.main()
