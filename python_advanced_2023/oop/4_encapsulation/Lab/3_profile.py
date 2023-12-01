class Profile:
    def __init__(self, username, password):
        self._set_username(username)
        self._set_password(password)

    def _set_username(self, username):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    def _get_username(self):
        return self.__username

    def _set_password(self, password):
        if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def _get_password(self):
        return self.__password

    def __str__(self):
        masked_password = '*' * len(self._get_password())
        return f'You have a profile with username: "{self._get_username()}" and password: {masked_password}'

#
# import unittest
#
# class Tests(unittest.TestCase):
#     def test_invalid_password(self):
#         with self.assertRaises(ValueError) as ve:
#             self.profile = Profile('My_username', 'My-password')
#         self.assertEqual(str(ve.exception), "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def test_invalid_username(self):
#         with self.assertRaises(ValueError) as ve:
#             self.profile = Profile('Too_long_username', 'Any')
#         self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")
#
#     def test_correct_profile(self):
#         self.profile = Profile("Username", "Passw0rd")
#         self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')
#
# if __name__ == "__main__":
#     unittest.main()
