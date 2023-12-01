from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.test_full_data = Trip(15_000, 2, True)
        self.test_one_traveler = Trip(15_000, 1, True)
        self.test_two_trav_not_family = Trip(15_000, 2, False)

    def test_successful_init_operation(self):
        self.assertEqual(self.test_full_data.budget, 15_000)
        self.assertEqual(self.test_full_data.travelers, 2)
        self.assertTrue(self.test_full_data.is_family)
        self.assertFalse(self.test_full_data.booked_destinations_paid_amounts)

    def test_unsuccessful_init_operation(self):
        with self.assertRaises(ValueError) as ve:
            self.test_full_data.travelers = 0
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_successful_is_family_operation(self):
        self.assertTrue(self.test_full_data.is_family)
        self.assertGreaterEqual(self.test_full_data.travelers, 2)

    def test_unsuccessful_one_traveler_is_family_operation(self):
        self.assertEqual(self.test_one_traveler.travelers, 1)
        self.assertFalse(self.test_one_traveler.is_family)

    def test_unsuccessful_two_travelers_is_family_operation(self):
        self.assertGreaterEqual(self.test_two_trav_not_family.travelers, 2)
        self.assertFalse(self.test_two_trav_not_family.is_family)

    def test_unsuccessful_book_a_trip_wrong_destination_operation(self):
        self.assertFalse(self.test_full_data.booked_destinations_paid_amounts)
        result = self.test_full_data.book_a_trip('Havana')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_unsuccessful_book_a_trip_not_enough_budget_operation(self):
        self.test_full_data.budget = 800
        result = self.test_full_data.book_a_trip('Bulgaria')
        self.assertTrue(self.test_full_data.is_family)
        self.assertEqual(result, 'Your budget is not enough!')

    def test_successful_book_a_trip_family_operation(self):
        self.test_full_data.budget = 1001
        result = self.test_full_data.book_a_trip('Bulgaria')
        self.assertTrue(self.test_full_data.is_family)
        test_str = f'Successfully booked destination Bulgaria! Your budget left is 101.00'
        self.assertEqual(result, test_str)

    def test_successful_book_a_trip_not_family_operation(self):
        self.test_one_traveler.budget = 501
        result = self.test_one_traveler.book_a_trip('Bulgaria')
        self.assertFalse(self.test_one_traveler.is_family)
        test_str = f'Successfully booked destination Bulgaria! Your budget left is 1.00'
        self.assertEqual(result, test_str)

    def test_unsuccessful_booking_status_false_membership_in_dict(self):
        self.assertFalse(self.test_full_data.booked_destinations_paid_amounts)
        result = self.test_full_data.booking_status()
        self.assertEqual(result, 'No bookings yet. Budget: 15000.00')

    def test_successful_booking_status_operation(self):
        self.test_full_data.budget = 900
        self.test_full_data.book_a_trip('Bulgaria')
        result = self.test_full_data.booking_status()
        expected_result = 'Booked Destination: Bulgaria\nPaid Amount: 900.00\nNumber of Travelers: 2\nBudget Left: 0.00'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
