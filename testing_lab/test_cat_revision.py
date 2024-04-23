class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTest(TestCase):

    def test_init__sets_correct_values(self):
        cat = Cat('Mara')
        self.assertEqual('Mara', cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test__size_increases_after_eating(self):
        cat = Cat('Mara')
        cat.eat()
        self.assertEqual(1, cat.size)

    def test__is_fed_after_eating(self):
        cat = Cat('Mara')
        cat.eat()
        self.assertTrue(cat.fed)

    def test__is_sleepy_after_eating(self):
        cat = Cat('Mara')
        cat.eat()
        self.assertTrue(cat.sleepy)

    def test__is_fed__raises_when_fed_again(self):
        cat = Cat('Mara')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test__cannot_sleep_if_not_fed__expect_raises(self):
        cat = Cat('Mara')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test__not_is_sleepy_after_sleep(self):
        cat = Cat('Mara')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
