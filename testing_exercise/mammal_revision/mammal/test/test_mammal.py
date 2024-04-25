from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def test__init__initializes_correctly(self):
        mammal = Mammal('Tulupi', 'cat', 'meow')
        self.assertEqual('Tulupi', mammal.name)
        self.assertEqual('cat', mammal.type)
        self.assertEqual('meow', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test__make_sound__returns_correct_string(self):
        mammal = Mammal('Tulupi', 'cat', 'meow')
        result = mammal.make_sound()
        self.assertEqual('Tulupi makes meow', result)

    def test__get_kingdom__returns_correct_result(self):
        mammal = Mammal('Tulupi', 'cat', 'meow')
        result = mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test__info__returns_correct_info(self):
        mammal = Mammal('Tulupi', 'cat', 'meow')
        result = mammal.info()
        self.assertEqual('Tulupi is of type cat', result)


if __name__ == "__main__":
    main()
