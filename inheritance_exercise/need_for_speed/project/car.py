from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


# zero test
from project.vehicle import Vehicle
from project.family_car import FamilyCar
import unittest


class Tests(unittest.TestCase):
    def test(self):
        vehicle = Vehicle(50, 150)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(FamilyCar.DEFAULT_FUEL_CONSUMPTION, 3)
        self.assertEqual(vehicle.fuel, 50)
        self.assertEqual(vehicle.horse_power, 150)
        self.assertEqual(vehicle.fuel_consumption, 1.25)
        vehicle.drive(100)
        self.assertEqual(vehicle.fuel, 50)
        family_car = FamilyCar(150, 150)
        family_car.drive(50)
        self.assertEqual(family_car.fuel, 0.0)
        family_car.drive(50)
        self.assertEqual(family_car.fuel, 0.0)
        self.assertEqual(family_car.__class__.__bases__[0].__name__, "Car")


if __name__ == "__main__":
    unittest.main()
