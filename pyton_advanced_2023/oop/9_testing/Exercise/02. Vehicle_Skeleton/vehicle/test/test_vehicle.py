from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(69, 420)

    def test_successful_init_operation(self):
        self.assertEqual(self.test_vehicle.fuel, 69)
        self.assertEqual(self.test_vehicle.horse_power, 420)
        self.assertEqual(self.test_vehicle.capacity, 69)
        self.assertEqual(self.test_vehicle.fuel_consumption, 1.25)

    def test_successful_drive_operation(self):
        track = 5
        self.test_vehicle.drive(track)
        self.assertTrue(track * 1.25 <= self.test_vehicle.fuel)
        self.assertEqual(self.test_vehicle.capacity - (track * 1.25), self.test_vehicle.fuel)

    def test_unsuccessful_drive_raise_exception(self):
        track = 100
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(track)

        self.assertTrue(track * 1.25 > self.test_vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successful_refuel_operation(self):
        fuel = 10
        self.test_vehicle.capacity = 100
        self.assertTrue(self.test_vehicle.fuel + fuel <= self.test_vehicle.capacity)
        self.test_vehicle.refuel(fuel)
        self.assertEqual(self.test_vehicle.fuel, 79)

    def test_unsuccessful_refuel_too_much_fuel_raise_exception(self):
        fuel = 100
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(fuel)
        self.assertEqual(str(ex.exception), "Too much fuel")
        self.assertTrue(self.test_vehicle.fuel + fuel > self.test_vehicle.capacity)

    def test_successful__str__operation(self):
        result = 'The vehicle has 420 horse power with 69 fuel left and 1.25 fuel consumption'
        self.assertEqual(result, str(self.test_vehicle))


if __name__ == '__main__':
    main()
