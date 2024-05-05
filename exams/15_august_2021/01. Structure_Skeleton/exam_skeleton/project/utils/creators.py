from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class FoodCreator:
    food_types = {
        'Bread': Bread,
        'Cake': Cake
    }

    def create_food(self, food_type: str, name: str, price: float):
        return self.__class__.food_types[food_type](name, price)


class DrinkCreator:
    drink_types = {
        'Tea': Tea,
        'Water': Water
    }

    def create_drink(self, drink_type: str, name: str, portion: float, brand: str):
        return self.__class__.drink_types[drink_type](name, portion, brand)


class TableCreator:
    table_types = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def create_table(self, table_type: str, table_number: int, capacity: int):
        return self.__class__.table_types[table_type](table_number, capacity)
