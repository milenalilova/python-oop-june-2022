from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train('TrainName', 3)

    def test_train_init(self):
        name = 'Train'
        capacity = 3
        train = Train(name, capacity)

        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_adds_passenger_and_returns_proper_string(self):
        passenger_name = 'Pesho'
        result = self.train.add(passenger_name)

        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_raises_when_capacity_is_reached(self):
        self.train.passengers = ['Pesho', 'Gosho', 'Prakash']

        with self.assertRaises(ValueError) as context:
            self.train.add('Josh')

        self.assertEqual('Train is full', str(context.exception))

    def test_add_raises_when_passenger_already_exists(self):
        passenger_name = 'Pesho'
        self.train.passengers = [passenger_name]

        with self.assertRaises(ValueError) as context:
            self.train.add(passenger_name)

        self.assertEqual(f'Passenger {passenger_name} Exists', str(context.exception))

    def test_remove_raises_when_passenger_does_not_exist(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove('Pesho')

        self.assertEqual('Passenger Not Found', str(context.exception))

    def test_remove_removes_passenger_and_returns_proper_string(self):
        self.train.passengers = ['Pesho', 'Ivan']

        result = self.train.remove('Pesho')

        self.assertEqual('Removed Pesho', result)
        self.assertEqual(1, len(self.train.passengers))
        self.assertTrue('Pesho' not in self.train.passengers)
        self.assertTrue('Ivan' in self.train.passengers)


    if __name__ == '__main__':
        main()
