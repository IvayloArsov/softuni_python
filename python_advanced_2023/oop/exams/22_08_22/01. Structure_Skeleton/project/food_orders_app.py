from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    @staticmethod
    def find_obj_by_param_in_arr(arr: list, attribute: str, value: str):
        """
        Search for an object in a list based on a specific attribute and value.

        Parameters:
        - arr: The list of objects to search through.
        - attribute: The parameter to compare against in each object.
        - value: The value to match against the specified parameter.

        Returns:
        - object or None: The first matching object found, or None if no match.
        """
        return next((item for item in arr if getattr(item, attribute, None) == value), None)

    def register_client(self, client_phone_number: str):
        client = self.find_obj_by_param_in_arr(self.clients_list, 'phone_number', client_phone_number)
        if client:
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join(str(meal.details()) for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = self.find_obj_by_param_in_arr(self.clients_list, 'phone_number', client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        ordered_meals = []
        total_bill = 0
        for name, quantity in meal_names_and_quantities.items():
            meal = self.find_obj_by_param_in_arr(self.menu, 'name', name)
            if not meal:
                raise Exception(f"{name} is not on the menu!")
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {name}!")

            meal.quantity -= quantity
            ordered_meal = meal.__class__(meal.name, meal.price, quantity)
            client.shopping_cart.append(ordered_meal)
            ordered_meals.append(name)
            total_bill += meal.price * quantity

        client.bill += total_bill
        return f"Client {client_phone_number} successfully ordered {', '.join(client.get_shopping_cart_details())} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_obj_by_param_in_arr(self.clients_list, 'phone_number', client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal_menu = self.find_obj_by_param_in_arr(self.menu, 'name', meal.name)
            meal_menu.quantity += meal.quantity

        client.bill = 0
        client.shopping_cart = []
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_obj_by_param_in_arr(self.clients_list, 'phone_number', client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        total_paid_money = client.bill
        receipt_id = self.receipt_id
        self.receipt_id += 1
        client.bill = 0
        client.shopping_cart = []
        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        number_of_listed_meals = len(self.menu)
        number_of_clients = len(self.clients_list)
        return f"Food Orders App has {number_of_listed_meals} meals on the menu and {number_of_clients} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# print(food_orders_app.finish_order('0899999999'))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)