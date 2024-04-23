class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTest(TestCase):

    def test__init__when_valid_props__expect_correct_values(self):
        worker = Worker('Milena', 1000, 2)
        self.assertEqual('Milena', worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(2, worker.energy)
        self.assertEqual(0, worker.money)

    def test__rest__expect_energy_to_be_incremented(self):
        worker = Worker('Milena', 1000, 2)
        worker.rest()
        self.assertEqual(3, worker.energy)

    def test__work__when_energy_is_0__expect_to_raise(self):
        worker = Worker('Milena', 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        # self.assertIsNotNone(ex)
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test__work__when_enough_energy__expect_money_to_be_increased_with_salary(self):
        worker = Worker('Milena', 1000, 2)

        worker.work()
        self.assertEqual(1000, worker.money)

        worker.work()
        self.assertEqual(2000, worker.money)

    def test__work__when_enough_energy__expect_energy_to_decrease(self):
        worker = Worker('Milena', 1000, 2)
        worker.work()

        self.assertEqual(1, worker.energy)

    def test__get_info__expect_correct_values(self):
        worker = Worker('Milena', 1000, 2)
        actual_info = worker.get_info()
        expected_info = f"{'Milena'} has saved {0} money."

        self.assertEqual(expected_info, actual_info)


if __name__ == "__main__":
    main()
