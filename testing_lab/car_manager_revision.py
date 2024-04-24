class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTest(TestCase):
    def test__init__with_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        self.assertEqual('Honda', car.make)
        self.assertEqual('Civic', car.model)
        self.assertEqual(10, car.fuel_consumption)
        self.assertEqual(100, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test__init__with_incorrect_make__raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', 'Civic', 10, 100)
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car(None, 'Civic', 10, 100)
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test__init__with_incorrect_model__raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', '', 10, 100)
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Honda', None, 10, 100)
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test__init__with_incorrect_fuel_consumption__raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Civic', 0, 100)
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Civic', -5, 100)
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test__init__with_incorrect_fuel_capacity__raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Civic', 10, 0)
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Civic', 10, -5)
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test__set__with_incorrect_make__raises(self):
        car = Car('Honda', 'Civic', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.make = None
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test__set__with_incorrect_model__raises(self):
        car = Car('Honda', 'Civic', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.model = None
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test__set__with_incorrect_fuel_consumption__raises(self):
        car = Car('Honda', 'Civic', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -5
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test__set__with_incorrect_fuel_capacity__raises(self):
        car = Car('Honda', 'Civic', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -5
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test__set__with_incorrect_fuel_amount__raises(self):
        car = Car('Honda', 'Civic', 10, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -5
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test__set__with_valid_make__sets_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.make = 'Toyota'
        self.assertEqual('Toyota', car.make)

    def test__set__with_valid_model__sets_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.model = 'Yaris'
        self.assertEqual('Yaris', car.model)

    def test__set__with_valid_fuel_consumption__sets_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.fuel_consumption = 20
        self.assertEqual(20, car.fuel_consumption)

    def test__set__with_valid_fuel_capacity__sets_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.fuel_capacity = 200
        self.assertEqual(200, car.fuel_capacity)

    def test__set__with_valid_fuel_amount__sets_correct_data(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.fuel_amount = 50
        self.assertEqual(50, car.fuel_amount)

    def test__refuel__with_invalid_fuel__raises(self):
        car = Car('Honda', 'Civic', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test__refuel__with_valid_fuel__increases_fuel_amount(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.refuel(40)
        self.assertEqual(40, car.fuel_amount)

    def test__refuel__with_valid_fuel__does_not_exceed_fuel_capacity(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.refuel(200)
        self.assertEqual(100, car.fuel_amount)

    def test__drive__raises_if_needed_fuel_amount_not_enough(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.refuel(100)

        with self.assertRaises(Exception) as ex:
            car.drive(2000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test__drive__decreases_fuel_amount_if_enough_fuel_amount(self):
        car = Car('Honda', 'Civic', 10, 100)
        car.refuel(100)
        car.drive(100)
        self.assertEqual(90, car.fuel_amount)


if __name__ == "__main__":
    main()
