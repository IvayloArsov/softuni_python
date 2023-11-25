from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.test_car = SecondHandCar('Camry', 'Sedan', 100_000, 30_000.)

    def test_successful_init_operation(self):
        self.assertEqual(self.test_car.model, 'Camry')
        self.assertEqual(self.test_car.car_type, 'Sedan')
        self.assertEqual(self.test_car.mileage, 100_000)
        self.assertFalse(self.test_car.repairs)

    def test_unsuccessful_init_zero_inputs(self):
        with self.assertRaises(ValueError) as ex:
            test_car = SecondHandCar('', '', 0, 0)
        self.assertTrue(str(ex.exception))

    def test_unsuccessful_price_operation(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car.price = 0.5
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_successful_price_operation(self):
        self.test_car.price = 1.1
        self.assertEqual(self.test_car.price, 1.1)

    def test_unsuccessful_mileage_operation_equal(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car.mileage = 100
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_unsuccessful_mileage_operation_less(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car.mileage = 99
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_successful_mileage_operation(self):
        self.test_car.mileage = 101
        self.assertEqual(101, self.test_car.mileage)

    def test_unsuccessful_promotional_price_operation_equal(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car.set_promotional_price(30_000)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_unsuccessful_promotional_price_operation_higher(self):
        with self.assertRaises(ValueError) as ex:
            self.test_car.set_promotional_price(100_000)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_successful_promotional_price_operation(self):
        result = self.test_car.set_promotional_price(25_000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_unsuccessful_need_repair_operation(self):
        result = self.test_car.need_repair(16_000, 'Gearbox')
        self.assertEqual(result, 'Repair is impossible!')

    def test_successful_need_repair_operation(self):
        result = self.test_car.need_repair(500, 'Stoplight')
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertIn('Stoplight', self.test_car.repairs)
        self.assertEqual(30_500.0, self.test_car.price)

    def test_unsuccessful__gt__operation(self):
        other = SecondHandCar('F150', 'Truck', 10_000, 90_000)
        result = self.test_car < other
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_successful__gt_operation_True(self):
        other = SecondHandCar('Avensis', 'Sedan', 250_000, 16_000.0)
        result = self.test_car > other
        self.assertTrue(result)

    def test_successful__gt_operation_False(self):
        other = SecondHandCar('Avensis', 'Sedan', 250_000, 16_000.0)
        result = self.test_car < other
        self.assertFalse(result)

    def test_successful__str__operation(self):
        result = str(self.test_car)
        info_str = 'Model Camry | Type Sedan | Milage 100000km\nCurrent price: 30000.00 | Number of Repairs: 0'
        self.assertEqual(result, info_str)

    def test_successful__str__operation_with_repairs(self):
        self.test_car.need_repair(500, 'Stoplight')
        result = str(self.test_car)
        info_str = 'Model Camry | Type Sedan | Milage 100000km\nCurrent price: 30500.00 | Number of Repairs: 1'
        self.assertEqual(result, info_str)

    def test_successful__str__operation_with_two_repairs(self):
        self.test_car.need_repair(500, 'Stoplight')
        self.test_car.need_repair(1, 'Diagnostics')
        result = str(self.test_car)
        info_str = 'Model Camry | Type Sedan | Milage 100000km\nCurrent price: 30501.00 | Number of Repairs: 2'
        self.assertEqual(result, info_str)


if __name__ == '__main__':
    main()
