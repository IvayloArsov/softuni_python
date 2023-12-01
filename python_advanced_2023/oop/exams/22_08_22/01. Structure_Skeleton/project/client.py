class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []
        self.bill: float = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or value[0] != '0' or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

    def get_shopping_cart_details(self):
        return [meal.name for meal in self.shopping_cart]
