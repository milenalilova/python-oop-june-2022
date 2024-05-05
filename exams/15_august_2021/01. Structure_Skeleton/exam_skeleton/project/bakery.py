from project.utils.creators import FoodCreator, DrinkCreator, TableCreator
from project.utils.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_creator = FoodCreator()
        self.drink_creator = DrinkCreator()
        self.table_creator = TableCreator()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_non_empty_string_or_white_space(value, 'Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if [f for f in self.food_menu if f.name == name]:
            raise Exception(f'{food_type} {name} is already in the menu!')
        food = self.food_creator.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if [d for d in self.drinks_menu if d.name == name]:
            raise Exception(f'{drink_type} {name} is already in the menu!')
        drink = self.drink_creator.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if [t for t in self.tables_repository if t.table_number == table_number]:
            raise Exception(f'Table {table_number} is already in the bakery!')
        table = self.table_creator.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.find_free_table(number_of_people)
        if table is not None:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.find_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        found_foods = []
        foods_not_found = []
        for food_name in food_names:
            food = self.find_item_by_name(food_name, self.food_menu)
            if not food:
                foods_not_found.append(food_name)
            else:
                table.order_food(food)
                found_foods.append(f'{food}')

        output = ''
        if found_foods:
            output += f'Table {table_number} ordered:' + '\n' + '\n'.join(found_foods)

        if foods_not_found:
            output += '\n' + f'{self.name} does not have in the menu:' + '\n' + '\n'.join(foods_not_found)

        return output.strip()

    def order_drink(self, table_number: int, *drinks_names):
        table = self.find_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        found_drinks = []
        drinks_not_found = []
        for drink_name in drinks_names:
            drink = self.find_item_by_name(drink_name, self.drinks_menu)
            if not drink:
                drinks_not_found.append(drink_name)
            else:
                table.order_drink(drink)
                found_drinks.append(f'{drink}')

        output = ''
        if found_drinks:
            output += f'Table {table_number} ordered:' + '\n' + '\n'.join(found_drinks)

        if drinks_not_found:
            output += '\n' + f'{self.name} does not have in the menu:' + '\n' + '\n'.join(drinks_not_found)

        return output.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        output = f'Table: {table_number}' + '\n'
        output += f'Bill: {bill:.2f}'
        return output.strip()

    def get_free_tables_info(self):
        free_tables_info = []
        for table in self.tables_repository:
            if not table.is_reserved:
                free_tables_info.append(table.free_table_info())
        return '\n'.join(free_tables_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_free_table(self, people_count):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= people_count:
                    return table

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    @staticmethod
    def find_item_by_name(item_name, items_list):
        for item in items_list:
            if item.name == item_name:
                return item
