from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incrementation(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Fruit', 'Meat', 'Seed']

    @property
    def weight_incrementation(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
