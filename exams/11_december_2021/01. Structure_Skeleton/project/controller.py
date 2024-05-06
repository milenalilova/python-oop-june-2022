from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

        self.car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(c.model == model for c in self.cars):
            raise Exception(f'Car {model} is already created!')

        car = self.car_factory.create_car(car_type, model, speed_limit)
        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f'Driver {driver_name} is already created!')

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f'Race {race_name} is already created!')

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_obj_by_name(driver_name, self.drivers)
        car = self.find_last_free_car_by_type(car_type)

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not car:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car:
            old_car = driver.car
            return driver.change_car(car, old_car)

        if not driver.car:
            car.is_taken = True
            car.driver = driver
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_obj_by_name(race_name, self.races)
        driver = self.find_obj_by_name(driver_name, self.drivers)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not driver.car:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.find_obj_by_name(race_name, self.races)

        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(self.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]
        output = ''
        for driver in winners:
            driver.number_of_wins += 1
            output += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}." + '\n'
        return output.strip()

    @staticmethod
    def find_obj_by_name(name, obj_list):
        for obj in obj_list:
            if obj.name == name:
                return obj

    def find_last_free_car_by_type(self, type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]
            if car.type == type:
                if not car.is_taken:
                    return car
