from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.test_mammal = Mammal('Goshko', 'cat', 'meow')

    def test_successful_init(self):
        self.assertEqual(self.test_mammal.name, 'Goshko')
        self.assertEqual(self.test_mammal.type, 'cat')
        self.assertEqual(self.test_mammal.sound, 'meow')
        self.assertEqual(self.test_mammal._Mammal__kingdom, 'animals')

    def test_successful_make_sound_operation(self):
        result = self.test_mammal.make_sound()
        self.assertEqual(result, 'Goshko makes meow')

    def test_successful_get_kingdom_operation(self):
        result = self.test_mammal.get_kingdom()
        self.assertEqual(result, 'animals')

    def test_successful_info_operation(self):
        result = self.test_mammal.info()
        self.assertEqual(result, 'Goshko is of type cat')


if __name__ == '__main__':
    main()
