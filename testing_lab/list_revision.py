class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test__init__sets_empty_list_if_not_args(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)

    def test__init__sets_only_ints_if_mix_args(self):
        int_list = IntegerList('pepe', 4.3)
        self.assertEqual([], int_list._IntegerList__data)

    def test__init__sets_correct_values_when_all_ints(self):
        int_list = IntegerList(3, 4, 5)
        self.assertEqual([3, 4, 5], int_list._IntegerList__data)

    def test__get_data__returns_correct_data(self):
        int_list = IntegerList(3, 4, 5, 'pepe', 2.3)
        self.assertEqual([3, 4, 5], int_list._IntegerList__data)

    def test__add__raises_if_element_not_int(self):
        int_list = IntegerList(3, 4, 5)
        with self.assertRaises(ValueError) as ex:
            int_list.add(5.3)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test__add__returns_correct_data_if_element_is_int(self):
        int_list = IntegerList(3, 4, 5)
        int_list.add(6)
        self.assertEqual([3, 4, 5, 6], int_list._IntegerList__data)

    def test__remove__index__raises_if_invalid_index(self):
        int_list = IntegerList(3, 4)
        with self.assertRaises(IndexError) as ex:
            int_list.remove_index(5)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test__remove__index__asserts_correct_element_at_given_index(self):
        int_list = IntegerList(3, 4, 5)
        self.assertEqual(4, int_list._IntegerList__data[1])

    def test__remove__index__deletes_given_index(self):
        int_list = IntegerList(3, 4, 5)
        int_list.remove_index(0)
        self.assertEqual([4, 5], int_list._IntegerList__data)

    def test__remove__index__returns_correct_element_at_given_index(self):
        int_list = IntegerList(3, 4, 5)
        el = int_list.remove_index(0)
        self.assertEqual(3, el)

    def test__get__raises_if_invalid_index(self):
        int_list = IntegerList(3, 4)
        with self.assertRaises(IndexError) as ex:
            int_list.get(5)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test__get__returns_element_at_given_index(self):
        int_list = IntegerList(3, 4, 5)
        el = int_list.get(2)
        self.assertEqual(5, el)

    def test__insert__raises_if_invalid_index(self):
        int_list = IntegerList(3, 4, 5)
        with self.assertRaises(IndexError) as ex:
            int_list.insert(5, 1)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test__insert__raises_if_element_not_int(self):
        int_list = IntegerList(3, 4, 5)
        with self.assertRaises(ValueError) as ex:
            int_list.insert(1, 1.5)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test__insert__inserts_element_at_given_index(self):
        int_list = IntegerList(3, 4, 5)
        int_list.insert(0, 1)
        self.assertEqual([1, 3, 4, 5], int_list._IntegerList__data)

        int_list.insert(1, 2)
        self.assertEqual([1, 2, 3, 4, 5], int_list._IntegerList__data)

    def test__get_biggest__returns_largest_int(self):
        int_list = IntegerList(3, 4, 5, 100, -500)
        biggest = int_list.get_biggest()
        self.assertEqual(100, biggest)

    def test__get_index__returns_elements_index(self):
        int_list = IntegerList(3, 4, 5, 100, -500)
        result = int_list.get_index(5)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
