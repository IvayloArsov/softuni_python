class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.__pin = pin
        self.balance = balance

    def get_id(self, entered_pin):
        if entered_pin == self.__pin:
            return self.__id

        return 'Wrong pin'

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return 'Pin changed'
        return 'Wrong pin'

#
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         a = Account(1234, 44, 4444)
#         self.assertEqual(a._Account__id, 1234)
#         self.assertEqual(a.balance, 44)
#         self.assertEqual(a._Account__pin, 4444)
#
#     def test_get_id_unsuccessfull(self):
#         a = Account(1234, 44, 4444)
#         res = a.get_id(1234)
#         self.assertEqual(res, "Wrong pin")
#
#     def test_get_id_successfull(self):
#         a = Account(1234, 44, 4444)
#         res = a.get_id(4444)
#         self.assertEqual(res, 1234)
#
#     def test_get_balance(self):
#         a = Account(1234, 44, 4444)
#         res = a.balance
#         self.assertEqual(res, 44)
#
#     def test_change_pin_successfull(self):
#         a = Account(1234, 44, 4444)
#         res = a.change_pin(4444, 1234)
#         self.assertEqual(res, "Pin changed")
#         self.assertEqual(a._Account__pin, 1234)
#
#
# if __name__ == "__main__":
#     unittest.main()
