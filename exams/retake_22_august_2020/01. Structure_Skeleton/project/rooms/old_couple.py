from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    ROOM_COST = 15

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, budget=pension_one + pension_two, members_count=2)
        self.room_cost = OldCouple.ROOM_COST
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.calculate_expenses(self.appliances)
