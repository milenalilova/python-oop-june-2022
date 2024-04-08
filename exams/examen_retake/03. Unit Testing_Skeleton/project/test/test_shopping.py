from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Test', 100)

    def test_init(self):
        self.assertEqual('Test', self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_raises_if_shop_name_invalid(self):
        invalid_name = 'test'
        with self.assertRaises(ValueError) as context:
            self.invalid_name = ShoppingCart(invalid_name, 100)
        self.assertEqual(str(context.exception), "Shop must contain only letters and must start with capital letter!")

        invalid_name_second = '0test'
        with self.assertRaises(ValueError) as context:
            self.invalid_name = ShoppingCart(invalid_name, 100)
        self.assertEqual(str(context.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_raises(self):
        with self.assertRaises(ValueError) as context:
            self.shopping_cart.add_to_cart('book', 150)
        self.assertEqual(str(context.exception), "Product book cost too much!")

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.add_to_cart('book', 100)
        self.assertEqual(str(context.exception), "Product book cost too much!")

    def test_add_product_adds_to_shopping_cart(self):
        result = self.shopping_cart.add_to_cart('book', 50)

        self.assertEqual(result, "book product was successfully added to the cart!")

    def test_remove_from_cart_raises(self):
        self.shopping_cart.add_to_cart('book', 50)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.remove_from_cart('cheese')
        self.assertEqual(str(context.exception), "No product with name cheese in the cart!")

    def test_remove_from_cart_works_properly(self):
        self.shopping_cart.add_to_cart('book', 50)
        remove_example = self.shopping_cart.remove_from_cart('book')
        self.assertEqual(remove_example, "Product book was successfully removed from the cart!")
        self.assertEqual({}, self.shopping_cart.products)

    def test_buy_products_raises(self):
        self.shopping_cart.add_to_cart('book', 80)
        self.shopping_cart.add_to_cart('cheese', 30)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.buy_products()
        self.assertEqual(str(context.exception), "Not enough money to buy the products! Over budget with 10.00lv!")

    def test_buy_products_works_properly(self):
        self.shopping_cart.add_to_cart('book', 80)

        result = self.shopping_cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 80.00lv.')

    def test_add(self, other):
        other_shopping_cart = ShoppingCart("New", 200)
        result = self.shopping_cart.__add__(self.shopping_cart.shop_name, other_shopping_cart)
        result_budget = self.shopping_cart.budget+other_shopping_cart.budget
        self.assertEqual(result_budget, 300)


        # new_shop_name = f"{self.shop_name}{other.shop_name}"
        # new_budget = self.budget + other.budget
        # new_shopping_cart = ShoppingCart(new_shop_name, new_budget)
        # new_shopping_cart.products.update(**self.products)
        # new_shopping_cart.products.update(**other.products)
        # return new_shopping_cart













if __name__ == '__main__':
    main()
