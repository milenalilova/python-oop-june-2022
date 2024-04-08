class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    #TODO create helper method for filtering
    @property
    def food(self):
        food_list = [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]
        if not food_list:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_supplies = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        if not water_supplies:
            raise IndexError("There are no water supplies left!")
        return water_supplies
    
    @property
    def painkillers(self):
        painkillers_list = [m for m in self.medicine if m.__class__.__name__ == "Painkiller"]
        if not painkillers_list:
            raise IndexError("There are no painkillers left!")
        return painkillers_list
    
    @property
    def salves(self):
        salves_list = [m for m in self.medicine if m.__class__.__name__ == "Salve"]
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        # TODO from property
        to_remove_medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(to_remove_medicine)
            to_remove_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        to_remove_supply = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(to_remove_supply)
            to_remove_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


# from project.supply.food_supply import FoodSupply
# from project.supply.water_supply import WaterSupply
# from project.survivor import Survivor
# from project.medicine.painkiller import Painkiller
# b = Bunker()
# s = Survivor("test", 10)
# b.add_survivor(s)
# b.add_medicine(Painkiller())
# print(b.medicine)
