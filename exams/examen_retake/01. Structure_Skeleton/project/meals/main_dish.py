from project.meals.meal import Meal


class MainDish(Meal):
    DEFAULT_QUANTITY = 50

    def __init__(self, name: str, price: float, quantity=DEFAULT_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"



