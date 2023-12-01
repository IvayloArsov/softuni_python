from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self):
        self.test_driver = TruckDriver('asdf', 10)

    def test_valid_initialization(self):
        self.assertEqual(self.test_driver.name, 'asdf')
        self.assertEqual(self.test_driver.money_per_mile, 10)
        self.assertFalse(self.test_driver.available_cargos)
        self.assertFalse(self.test_driver.earned_money)
        self.assertFalse(self.test_driver.miles)

    def test_invalid_earned_money_raises_ve(self):
        with self.assertRaises(ValueError) as ex:
            self.test_driver.earned_money = -1
        self.assertEqual(str(ex.exception), f"{self.test_driver.name} went bankrupt.")

    def test_invalid_add_cargo_offer_already_added(self):
        self.test_driver.add_cargo_offer('qwerty', 1000)
        with self.assertRaises(Exception) as ex:
            self.test_driver.add_cargo_offer('qwerty', 1000)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_valid_add_cargo_offer_operation(self):
        result = self.test_driver.add_cargo_offer('qwerty', 1000)
        self.assertEqual(result, "Cargo for 1000 to qwerty was added as an offer.")

    def test_drive_best_cargo_offer_with_available_cargo(self):
        self.test_driver.add_cargo_offer("DestinationA", 200)

        result = self.test_driver.drive_best_cargo_offer()

        self.assertEqual(result, "asdf is driving 200 to DestinationA.")
        self.assertEqual(self.test_driver.earned_money, 2000)
        self.assertEqual(self.test_driver.miles, 200)

    def test_drive_best_cargo_offer_without_available_cargo(self):
        result = self.test_driver.drive_best_cargo_offer()

        self.assertEqual(result, "There are no offers available.")
        self.assertEqual(self.test_driver.earned_money, 0)
        self.assertEqual(self.test_driver.miles, 0)

    def test_drive_best_cargo_offer_with_multiple_cargo_offers(self):
        self.test_driver.add_cargo_offer("DestinationA", 200)
        self.test_driver.add_cargo_offer("DestinationB", 300)
        self.test_driver.add_cargo_offer("DestinationC", 150)

        result = self.test_driver.drive_best_cargo_offer()

        self.assertIn(result, ["asdf is driving 200 to DestinationA.", "asdf is driving 300 to DestinationB.",
                               "asdf is driving 150 to DestinationC."])
        self.assertEqual(self.test_driver.earned_money, 2980)
        self.assertEqual(self.test_driver.miles, 300)

    def test_check_for_activities_250_miles(self):
        self.test_driver.add_cargo_offer('qwerty', 250)
        self.test_driver.drive_best_cargo_offer()
        self.assertEqual(self.test_driver.earned_money, 2480)

    def test_check_for_activities_1_000_miles(self):
        self.test_driver.add_cargo_offer('qwerty', 1_000)
        self.test_driver.drive_best_cargo_offer()
        self.assertEqual(self.test_driver.earned_money, 9875)

    def test_check_for_activities_1_500_miles(self):
        self.test_driver.add_cargo_offer('qwerty', 1_500)
        self.test_driver.drive_best_cargo_offer()
        self.assertEqual(self.test_driver.earned_money, 14335)

    def test_check_for_activities_10_000_miles(self):
        self.test_driver.add_cargo_offer('qwerty', 10_000)
        self.test_driver.drive_best_cargo_offer()
        self.assertEqual(self.test_driver.earned_money, 88250)

    def test_check_for_activities_any_miles_low_price_raises_value_error(self):
        self.test_driver.money_per_mile = 1
        self.test_driver.add_cargo_offer('qwerty', 10_000)
        with self.assertRaises(ValueError) as ex:
            self.test_driver.drive_best_cargo_offer()
        self.assertEqual(str(ex.exception), "asdf went bankrupt.")

    def test_valid__repr__operation(self):
        self.test_driver.add_cargo_offer('qwerty', 10_000)
        self.test_driver.drive_best_cargo_offer()
        result = repr(self.test_driver)
        self.assertEqual(result, "asdf has 10000 miles behind his back.")


if __name__ == '__main__':
    main()
