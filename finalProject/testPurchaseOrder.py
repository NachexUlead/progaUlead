import unittest
from product import Product
from purchaseOrder import PurchaseOrder
from taxes import calculateTax, validateState


class TestPurchaseOrder(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Product 1", "P1", 1500.0)
        self.product2 = Product("Product 2", "P2", 50.0)
        self.products = [self.product1, self.product2]
        self.order = PurchaseOrder(self.products)

    def testStateValidation(self):
        self.assertTrue(validateState("CA"))
        self.assertFalse(validateState("ZZ"))

    def testInvalidState(self):
        with self.assertRaises(ValueError):
            self.order.calculateFinalPrice("ZZ")

    def testTaxCalculation(self):

        # State NH (0% tax)
        self.assertEqual(calculateTax("NH", 1550.0), 0.0)

        # State MA (18% tax)
        self.assertAlmostEqual(calculateTax("MA", 1550.0), 279.0)

        # State IL (<1000 no tax, >1000 and <10000 tax 12%)
        self.assertAlmostEqual(calculateTax("IL", 1550.0), 186.0)

        # State KY (>1000 and <10000 tax 13%)
        self.assertAlmostEqual(calculateTax("KY", 1550.0), 201.5)

    def testFinalPrice(self):
        self.assertEqual(sum([product.getPrice() for product in self.products]), 1550.0)
        self.assertAlmostEqual(self.order.calculateFinalPrice("CA"), 1829.0)


if __name__ == "__main__":
    unittest.main()
