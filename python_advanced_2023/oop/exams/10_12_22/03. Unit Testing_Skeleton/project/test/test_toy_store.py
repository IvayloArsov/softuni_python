from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def test_valid_init_operation(self):
        toy_store = ToyStore()
        self.assertIsInstance(toy_store, ToyStore)
        self.assertIsNotNone(toy_store.toy_shelf)
        self.assertIsInstance(toy_store.toy_shelf, dict)
        self.assertEqual(len(toy_store.toy_shelf), 7)
        self.assertDictEqual(toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy_shelf_not_exist(self):
        shelf = "Z"
        toy_name = "Teddy Bear"

        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_add_toy_already_in_shelf(self):
        shelf = "A"
        toy_name = "Robot"

        self.toy_store.toy_shelf[shelf] = toy_name

        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        shelf = "B"
        toy_name = "Doll"
        self.toy_store.toy_shelf[shelf] = "Robot"

        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_add_toy_valid_operation(self):
        shelf = "C"
        toy_name = "Car"

        result = self.toy_store.add_toy(shelf, toy_name)

        self.assertEqual(result, f"Toy:{toy_name} placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf[shelf], toy_name)

    def test_remove_toy_shelf_not_exist(self):
        shelf = "Z"
        toy_name = "Teddy Bear"

        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_toy_not_in_shelf(self):
        shelf = "A"
        toy_name = "Robot"
        self.toy_store.toy_shelf[shelf] = "Doll"

        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_valid_operation(self):
        shelf = "B"
        toy_name = "Doll"
        self.toy_store.toy_shelf[shelf] = toy_name
        result = self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual(result, f"Remove toy:{toy_name} successfully!")
        self.assertIsNone(self.toy_store.toy_shelf[shelf])


if __name__ == '__main__':
    main()
