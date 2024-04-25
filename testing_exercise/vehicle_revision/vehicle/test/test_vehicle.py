from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def test__init__initializes_correct_values(self):
        vehicle = Vehicle(50, 100)
        self.assertEqual(50, vehicle.fuel)
        self.assertEqual(50, vehicle.capacity)
        self.assertEqual(100, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test__drive__raises_if_fuel_needed_not_enough(self):
        vehicle = Vehicle(50, 100)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(50)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test__drive__decreases_fuel_with_fuel_needed_if_fuel_enough(self):
        vehicle = Vehicle(50, 100)
        vehicle.drive(5)
        self.assertEqual(43.75, vehicle.fuel)

    def test__refuel__raises_if_fuel_capacity_exceeded(self):
        vehicle = Vehicle(50, 100)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(50)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test__refuel__increases_fuel_if_enough_capacity(self):
        vehicle = Vehicle(50, 100)
        vehicle.drive(5)
        vehicle.refuel(1)
        self.assertEqual(44.75, vehicle.fuel)

    def test__str__returns_correct_string(self):
        vehicle = Vehicle(50, 100)
        result = vehicle.__str__()
        self.assertEqual('The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption', result)


if __name__ == "__main__":
    main()
