from List.extended_list import IntegerList

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(9, 8, 'asdf', 6, True, [], {}, 2.3)

    def test_constructor(self):
        self.assertEqual(self.integer_list._IntegerList__data, [9, 8, 6])

    def test_get_data(self):
        self.assertEqual(self.integer_list._IntegerList__data, [9, 8, 6])

    def test_add_exception(self):
        self.assertEqual(3, len(self.integer_list.get_data()))
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add('abc')
        self.assertEqual(str(ex.exception), "Element is not Integer")
        self.assertEqual(3, len(self.integer_list.get_data()))

    def test_add_operation(self):
        self.integer_list.add(1)
        self.assertIn(1, self.integer_list._IntegerList__data)

    def test_remove_index_operation(self):
        result = self.integer_list.remove_index(0)
        self.assertEqual(result, 9)
        self.assertEqual(self.integer_list._IntegerList__data, [8, 6])

    def test_remove_index_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(69)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_operation(self):
        result = self.integer_list.get(2)
        self.assertEqual(result, 6)
        self.assertEqual(self.integer_list._IntegerList__data[2], 6)

    def test_get_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(69)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_operation(self):
        self.integer_list.insert(2, 69)
        self.assertEqual(self.integer_list._IntegerList__data, [9, 8, 69, 6])

    def test_insert_index_exceptions(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(5, 420)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_value_exceptions(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, '69')
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_get_biggest_operation(self):
        self.assertEqual(self.integer_list.get_biggest(), max(self.integer_list._IntegerList__data))

    def test_get_index_operation(self):
        self.assertEqual(self.integer_list.get_index(9), 0)


if __name__ == '__main__':
    main()
