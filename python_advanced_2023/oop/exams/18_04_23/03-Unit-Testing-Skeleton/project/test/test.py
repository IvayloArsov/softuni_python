from project.robot import Robot

from unittest import TestCase, main


class TestRobotClass(TestCase):
    def test_correct_init(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.assertEqual(self.robot.robot_id, "R1")
        self.assertEqual(self.robot.category, 'Education')
        self.assertEqual(self.robot.available_capacity, 200)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

        self.robot2 = Robot('R1', 'Education', 200, 0)
        self.assertEqual(self.robot2.robot_id, "R1")
        self.assertEqual(self.robot2.category, 'Education')
        self.assertEqual(self.robot2.available_capacity, 200)
        self.assertEqual(self.robot2.price, 0)
        self.assertEqual(self.robot2.hardware_upgrades, [])
        self.assertEqual(self.robot2.software_updates, [])

    def test_wrong_category__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('R1', 'Wrong', 200, 100)
        self.assertEqual(str(ve.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_negative_price__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('R1', 'Education', 200, -1)
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade__not_existing_component__should_upgrade_successfully(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.robot.upgrade('SSD1TB', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['SSD1TB'])
        self.assertEqual(self.robot.price, 250)

        result = self.robot.upgrade('RAM64', 100)
        self.assertEqual(result, 'Robot R1 was upgraded with RAM64.')
        self.assertEqual(self.robot.hardware_upgrades, ['SSD1TB', 'RAM64'])
        self.assertEqual(self.robot.price, 400)

    def test_upgrade_with_existing_component__should_not_upgrade(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.robot.upgrade('RAM64', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['RAM64'])
        self.assertEqual(self.robot.price, 250)

        result = self.robot.upgrade('RAM64', 100)
        self.assertEqual(result, "Robot R1 was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ['RAM64'])
        self.assertEqual(self.robot.price, 250)

    def test_update__not_existing_version_and_enough_capacity__should_update_successfully(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])
        self.assertEqual(self.robot.available_capacity, 150)

        result = self.robot.update(2.23, 50)
        self.assertEqual(result, 'Robot R1 was updated to version 2.23.')
        self.assertEqual(self.robot.software_updates, [2.22, 2.23])
        self.assertEqual(self.robot.available_capacity, 100)

    def test_update__existing_version_and_enough_capacity__should_not_update(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])
        result = self.robot.update(2.22, 50)
        self.assertEqual(result, 'Robot R1 was not updated.')
        self.assertEqual(self.robot.software_updates, [2.22])
        self.assertEqual(self.robot.available_capacity, 150)

    def test_update__lower_version_and_enough_capacity__should_not_update(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])
        result = self.robot.update(2.20, 50)
        self.assertEqual(result, 'Robot R1 was not updated.')
        self.assertEqual(self.robot.software_updates, [2.22])
        self.assertEqual(self.robot.available_capacity, 150)

    def test__gt__should_return_first_robot_is_more_expensive(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Education', 200, 99.99)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 is more expensive than Robot with ID R2.")

    def test__gt__should_return_first_robot_is_cheaper(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Education', 200, 100.01)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 is cheaper than Robot with ID R2.")

    def test__gt__should_return_robots_are_equal(self):
        self.robot = Robot('R1', 'Education', 200, 100.01)
        self.other_robot = Robot('R2', 'Education', 200, 100.01)

        result = self.robot > self.other_robot
        self.assertEqual(result, "Robot with ID R1 costs equal to Robot with ID R2.")

if __name__ == '__main__':
    main()