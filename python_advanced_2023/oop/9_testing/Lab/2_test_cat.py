from unittest import TestCase, main


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


class CatTests(TestCase):
    def test_size_increased_after_eating(self):
        cat = Cat("Whiskers")
        initial_size = cat.size
        cat.eat()
        self.assertEqual(cat.size, initial_size + 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Mittens")
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cannot_eat_if_already_fed_raises_error(self):
        cat = Cat("Fluffy")
        cat.eat()
        with self.assertRaises(Exception):
            cat.eat()

    def test_cannot_fall_asleep_if_not_fed_raises_error(self):
        cat = Cat("Smokey")
        with self.assertRaises(Exception):
            cat.sleep()

    def test_not_sleepy_after_sleeping(self):
        cat = Cat("Shadow")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    main()
