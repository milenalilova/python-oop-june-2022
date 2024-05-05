from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

bread = Bread('White', 3)
cake = Cake('Opera', 6)
print(bread)
print(cake)

tea = Tea('Assam', 200, 'Twinings')
water = Water('Still', 500, 'Capes')
print(tea)
print(water)

inside_table = InsideTable(5, 4)
outside_table = OutsideTable(55, 6)
print(inside_table.table_number)
print(inside_table.capacity)
print(inside_table.food_orders)
print(inside_table.drink_orders)
print(inside_table.number_of_people)
print(inside_table.is_reserved)
print(inside_table.table_type)

print()
# print(outside_table.table_number)
# print(outside_table.capacity)
# print(outside_table.food_orders)
# print(outside_table.drink_orders)
# print(outside_table.number_of_people)
# print(outside_table.is_reserved)
# print(outside_table.table_type)

inside_table.reserve(4)
print(inside_table.is_reserved)
print(inside_table.number_of_people)
inside_table.order_food(bread)
inside_table.order_drink(water)
print(inside_table.food_orders)
print(inside_table.drink_orders)
print(inside_table.get_bill())
inside_table.clear()
print()
print(inside_table.table_number)
print(inside_table.capacity)
print(inside_table.food_orders)
print(inside_table.drink_orders)
print(inside_table.number_of_people)
print(inside_table.is_reserved)
print(inside_table.table_type)
print()
print(inside_table.free_table_info())

print()

bakery = Bakery('Bakery')
print(bakery.name)
print(bakery.food_menu)
print(bakery.drinks_menu)
print(bakery.tables_repository)
print(bakery.total_income)
print()

bakery.add_food('Bread', 'Granary', 3)
print(bakery.food_menu)
bakery.add_drink('Tea', 'Earl Grey', 150, 'PG Tips')
print(bakery.drinks_menu)
bakery.add_table('InsideTable', 5, 6)
print(bakery.tables_repository)
print()

print(bakery.reserve_table(8))
print()
print(bakery.food_menu)
print(bakery.order_food(5, 'Earl Grey', 'Granary'))
print()

print(bakery.drinks_menu)
print(bakery.order_drink(5, 'Earl Grey', 'Granary'))
print(bakery.leave_table(5))
print()
print(bakery.get_free_tables_info())
print()
print(bakery.get_total_income())

