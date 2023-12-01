from CarManager.car_manager import Car

from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self):
        self.test_car = Car('Renault', 'Captur', 5, 50)

    def test_succ_constructor_init(self):
        self.assertEqual(self.test_car.make, 'Renault')
        self.assertEqual(self.test_car.model, 'Captur')
        self.assertEqual(self.test_car.fuel_consumption, 5)
        self.assertEqual(self.test_car.fuel_capacity, 50)
        self.assertEqual(self.test_car.fuel_amount, 0)

    def test_unsucc_make_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.make = None
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_succ_make_operation(self):
        result = self.test_car.make = 'Lada'
        self.assertEqual(self.test_car.make, 'Lada')

    def test_unsucc_model_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.model = 0
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_succ_model_operation(self):
        result = self.test_car.model = 'Niva'
        self.assertEqual(self.test_car.model, 'Niva')

    def test_unsucc_fuel_consumption_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_consumption = -1
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_succ_fuel_consumption_operation(self):
        result = self.test_car.fuel_consumption = 6
        self.assertEqual(self.test_car.fuel_consumption, 6)

    def test_unsucc_fuel_capacity_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_capacity = -5
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_succ_fuel_capacity_operation(self):
        new_capacity = 15
        self.test_car.fuel_capacity = new_capacity
        self.assertEqual(self.test_car.fuel_capacity, new_capacity)

    def test_unsucc_fuel_amount_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_succ_fuel_amount_operation(self):
        result = self.test_car.fuel_amount = 1
        self.assertEqual(self.test_car.fuel_amount, 1)

    def test_unsucc_refuel_wrong_value(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_succ_refuel_over_max_value_operation(self):
        refuel_value = self.test_car.fuel_capacity + 1
        result = self.test_car.refuel(refuel_value)
        self.assertTrue(refuel_value > self.test_car.fuel_capacity)
        self.assertEqual(self.test_car.fuel_amount, 50)

    def test_succ_refuel_with_low_value(self):
        result = self.test_car.refuel(1)
        self.assertEqual(self.test_car.fuel_amount, 1)

    def test_unsucc_drive_large_distance(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.drive(500)
        self.assertTrue(500 > self.test_car.fuel_amount)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_succ_drive_small_distance(self):
        self.test_car.refuel(50)
        self.test_car.drive(1000)
        self.assertEqual(self.test_car.fuel_amount, 0)


if __name__ == '__main__':
    main()
