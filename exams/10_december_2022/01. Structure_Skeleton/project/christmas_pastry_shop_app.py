from project.core.booth_creator import BoothCreator
from project.core.delicacy_creator import DelicacyCreator
from project.core.validator import Validator


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

        self.delicacy_names = set()
        self.booth_numbers = set()

        self.delicacy_creator = DelicacyCreator()
        self.booth_creator = BoothCreator()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validator.validate_value_is_unique(name, self.delicacy_names, f'{name} already exists!')

        delicacy = self.delicacy_creator.create_delicacy(type_delicacy, name, price)
        self.delicacies.append(delicacy)
        self.delicacy_names.add(name)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validator.validate_value_is_unique(booth_number,
                                           self.booth_numbers,
                                           f'Booth number {booth_number} already exists!')

        booth = self.booth_creator.create_booth(type_booth, booth_number, capacity)
        self.booths.append(booth)
        self.booth_numbers.add(booth_number)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_first_free_booth(number_of_people)
        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        delicacy = self.__find_delicacy_by_name(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f'Booth {booth_number}:' + '\n' + f'Bill: {bill:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'

    def __find_first_free_booth(self, peoples_count):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= peoples_count:
                return booth
        raise Exception(f'No available booth for {peoples_count} people!')

    def __find_booth_by_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        raise Exception(f'Could not find booth {booth_number}!')

    def __find_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        raise Exception(f'No {delicacy_name} in the pastry shop!')
